import os
import jwt
from . import validators
from flask import Flask, jsonify, request
import psycopg2
import datetime

import smtplib
from email.mime.text import MIMEText
from flask_cors import CORS

env = os.getenv('FLASK_DEBUG', '1')

if env == '1':
    from dotenv import load_dotenv
    load_dotenv(verbose=True)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 100 * 1000
CORS(app)


@app.route('/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}

def create_app():
    return app

@app.route('/rrhh/agendarEntrevista', methods=['POST'])
def agendar_entrevista():
    form = validators.agendarEntrevista(request.form)
    if not form.validate():
        return {'estatus': 400, 'error': form.errors, 'mensaje': 'Error con los campos.'}, 400

    try:
        auth_header = request.headers.get('Authorization')
        if auth_header: 
            token = auth_header.replace('Bearer ', '')
            token = decode_token(token)
            if 'error' in token:
                # El token es inválido o ha expirado
                return jsonify({'estatus': 401, 'error': token['error'], 'mensaje': token['mensaje']}), 401
            else:
                # verificar si el usuario es admin

                user_type = token['tipoUsuario']
                if user_type != 1:
                    return {'estatus': 403, 'error': 'Usuario sin permisos', 'mensaje': 'Error, usuario sin permisos'}, 403
                
                usuarioAdministrador = token['idUsuario']
        else:
            # No hay un token en la cabecera
            return jsonify({'estatus': 401, 'error': 'Usuario no autenticado', 'mensaje': 'Error, usuario no autorizado'}), 401
        
        try:
            # Conexion a la base de datos PostgreSQL
            conn = psycopg2.connect(
                dbname = os.getenv('PG_DATABASE'),
                user = os.getenv('PG_USER'),
                password = os.getenv('PG_PASS'),
                host = os.getenv('PG_HOST'),
                port = os.getenv('PG_PORT')
            )  
            # Se crea un cursor para ejecutar consultas SQL
            cur = conn.cursor()
            # Se verifica si el cui del usuario administrativo existe
            cur.execute("SELECT id_personal_administrativo from personal_administrativo where id_usuario = "+usuarioAdministrador+";")
            if cur.rowcount > 0:        
                
                # Se debe enviar un correo antes al candidato para agendar la reunion
                # Se debe verificar el correo electronico
                respuesta = enviar_correo(form.correo.data,'Cita agendada',"Se registro la cita de la entrevista exitosamente. Candidato: " + form.nombres.data + ". Fecha de la cita: "+
                    str(form.fechaCita.data))
                if respuesta == 0:
                    return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, no existe el correo electronico '}), 500


                # Se obriene el id del personal administrativo
                rows = cur.fetchall()
                for row in rows:
                    usuarioAdministrador = row[0]
                # Se verifica que la fecha sea valida, osea mayor a la fecha actual
                if(datetime.datetime.now() < form.fechaCita.data):
                    sql = "INSERT INTO entrevista(fecha_hora_cita, nombres_candidato, apellidos_cantidato, correo, id_personal_administrativo) VALUES (%s,%s, %s, %s, %s)"
                    values = (form.fechaCita.data,form.nombres.data, form.apellidos.data, form.correo.data, usuarioAdministrador)
                    cur.execute(sql, values)
                    
                    conn.commit()
                    print("Se registro la cita de la entrevista exitosamente en la tabla entrevista")
                else:
                    return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, la fecha de la cita es invalida. '}), 500
  
            else:
                return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, el cui del usuario administrador no existe en la base de datos'}), 500
            
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()
        respuesta = {
            "estatus": 200,
            "mensaje": "Se registro la cita de la entrevista exitosamente. Candidato: " + form.nombres.data + ". Fecha de la cita: "+
            str(form.fechaCita.data)
        }
        
        return jsonify(respuesta), 200
    
    except Exception as e:
        print(e)
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400
    

def decode_token(token):
    try:
        secret_key = os.getenv('JWT_KEY')
        payload = jwt.decode(token, secret_key, algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado, iniciar sesión de nuevo', 'mensaje': 'Error, con el token'}

    except jwt.InvalidTokenError:
        return {'error': 'Token invalidó, iniciar sesión de nuevo', 'mensaje': 'Error, con el token'}
    


def enviar_correo(destinatario, asunto, mensaje):
    # Configuración del servidor SMTP
    servidor_smtp = "smtp.gmail.com"  # Cambia esto si usas otro proveedor de correo electrónico
    puerto_smtp = 587  # Puerto de servidor SMTP para TLS

    # Credenciales del remitente
    remitente = "mynorreneruizguerra@gmail.com"
    password = "omvixtfbeilsyccc"

    # Creación del mensaje
    mensaje = MIMEText(mensaje)
    mensaje['Subject'] = asunto
    mensaje['From'] = remitente
    mensaje['To'] = destinatario

    # Conexión con el servidor SMTP y envío del mensaje
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, password)
    try:
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        print("El correo electrónico se envió exitosamente")
        return 1
    except smtplib.SMTPException as e:
        print("Error al enviar el correo electrónico:", e)
        return 0

    # Cierre de la conexión con el servidor SMTP
    servidor.quit()
    

    