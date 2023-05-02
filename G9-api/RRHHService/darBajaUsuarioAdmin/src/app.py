import os
import jwt
from . import validators
from flask import Flask, jsonify, request
import psycopg2

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


@app.route('/rrhh/eliminarUsuarioAdmin', methods=['PUT'])
def eliminar_usuario():

    form = validators.eliminarUsuario(request.form)
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
            if cur.rowcount > 0:
                cur.execute("SELECT cui from Usuario where cui = "+form.cui.data+" and estado = 1;")
                if cur.rowcount > 0:
                    # Se actualiza el estado de la tabla Usuario a 0 = Deshabilitado
                    sql = "UPDATE Usuario SET estado =  %s WHERE cui = %s and tipo ='A'"
                    cur.execute(sql, (0, form.cui.data))
                    conn.commit()
                    print("Se dio de baja de manera exitosa")
                else:               
                    return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, el usuario actualmente se encuenta dado de baja'}), 500
            else:
                return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error, el usuario no existe'}), 500
            
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()

        respuesta = {
            "estatus": 200,
            "mensaje": "Se ha dado de baja a el usuario administrativo exitosamente"
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
    



    
    

    