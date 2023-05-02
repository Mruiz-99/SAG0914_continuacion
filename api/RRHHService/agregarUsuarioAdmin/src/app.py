import os
import jwt
from . import validators
from flask import Flask, jsonify, request
import psycopg2
import datetime
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


@app.route('/rrhh/agregarUsuario', methods=['POST'])
def agragar_usuario():

    form = validators.agregarUsuarios(request.form)
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
        else: 
            # No hay un token en la cabecera
            return jsonify({'estatus': 401, 'error': 'Usuario no autenticado', 'mensaje': 'Error, usuario no autorizado'}), 401
         
        if form.confirmarPassword.data != form.password.data:
            # No coinciden las contraseñas
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, las contraseñas difieren'}), 500
             

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
            
            cur.execute("SELECT cui from Usuario where cui = "+form.cui.data+";")
            if cur.rowcount == 0:
                # Estado predeterminado => 1 = habilitado
                sql = "INSERT INTO Usuario(cui, nombres, apellidos, correo, contrasena, fecha_nacimiento, tipo, estado) VALUES (%s,%s, %s, %s, %s, %s,%s,%s)"
                values = (form.cui.data,form.nombres.data, form.apellidos.data, form.correo.data, form.password.data, form.fechaNacimiento.data, 'A', 1)
                cur.execute(sql, values)
                conn.commit()
                print("Se registro el usuario en la tabla usuario")
            else:
                print("El usuario ya existe en la tabla usuario")
            # Se verifica que el departamento que se desea asignar al usuario exista en la tabla Departamento
            cur.execute("SELECT id_departamento from Departamento where nombre = '"+form.areaAsignada.data+"';")
            if cur.rowcount == 0:
                return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, el departamento no existe'}), 500
            else:
                rows = cur.fetchall()
                for row in rows:
                    idDepartamento = row[0]
            # Se verifica que el usuario exista en la tabla Personal_administrativo
            cur.execute("SELECT * from Personal_administrativo where id_usuario = "+form.cui.data+";")
            if cur.rowcount == 0:
                sql = "INSERT INTO personal_administrativo(fecha_contratacion, sueldo, id_usuario, id_departamento) VALUES (%s,%s, %s, %s)"
                values = (datetime.date.today().strftime('%Y/%m/%d'), form.sueldo.data, form.cui.data, idDepartamento)
                print('aun se ejecuta')
                cur.execute(sql, values)
                conn.commit()
                print("Se creo el usuario administrativo")
            else:
                return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, el usuario ya existe'}), 500

        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()

        respuesta = {
            "estatus": 200,
            "mensaje": "Se ha registrado el usuario administrativo exitosamente"
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