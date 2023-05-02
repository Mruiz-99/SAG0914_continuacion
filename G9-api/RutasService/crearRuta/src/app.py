import os
import jwt
from . import validators
from flask import Flask, jsonify, request
import psycopg2
import datetime


env = os.getenv('FLASK_DEBUG', '1')

if env == '1':
    from dotenv import load_dotenv
    load_dotenv(verbose=True)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 100 * 1000

@app.route('/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}

def create_app():
    return app

@app.route('/rutas/crearRuta', methods=['POST'])
def crear_ruta():
    form = validators.crearRuta(request.form)
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
                zonas = eval(form.zonas.data)
                if len(zonas) >5:
                    return jsonify({'estatus': 502, 'error': 'Error en los parametros de la peticion', 'mensaje': 'Error, el maximo de zonas a registrar son 5 por cada ruta y 1 la minima'}), 502

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

            cur.execute("SELECT nombre from Ruta where nombre = '"+form.nombre.data+"';")
            if cur.rowcount == 0:
                cur.execute("SELECT zonas from Ruta ;")
                results = cur.fetchall()
                results_clean = [r[0].strip('()') for r in results]
                for row in results_clean:
                    row = row.split(',')
                    for numero in row:
                        if int(numero) in zonas:
                            return jsonify({'estatus': 502, 'error': 'Error en los parametros de la peticion', 'mensaje': 'Error, una de las zonas ingresadas ya ha sido asignada a una ruta'}), 502
                i = 0
                for zona in zonas:
                    if i == 0:
                        zonasInsert = str(zona)
                    else:
                        zonasInsert = zonasInsert + ','+str(zona)
                    i = i +1
                sql = "INSERT INTO Ruta(nombre,zonas) VALUES(%s,%s);"
                values = (form.nombre.data,zonasInsert )
                cur.execute(sql,values)
                conn.commit()
            else:
                return jsonify({'estatus': 502, 'error': 'Error en los parametros de la peticion', 'mensaje': 'Error, el nombre de la ruta actualmente se encuentra registrada'}), 502
            
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()

        respuesta = {
            "estatus": 200,
            "mensaje": "Se creo la ruta de manera exitosa"
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
    



    
    

    