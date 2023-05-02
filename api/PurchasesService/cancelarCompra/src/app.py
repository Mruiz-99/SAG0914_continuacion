import os
import jwt
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

def create_app():
    return app

@app.route('/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}


@app.route('/buy/emptyProductCart', methods=['DELETE'])
def cancelar_compra():
    try:
        auth_header = request.headers.get('Authorization')
        cui=''
        if auth_header: 
            token = auth_header.replace('Bearer ', '')
            token = decode_token(token)
            if 'error' in token:
                # El token es inválido o ha expirado
                return jsonify({'estatus': 401, 'error': token['error'], 'mensaje': token['mensaje']}), 401
            else:
                user_type = token['tipoUsuario']
                if user_type != 'E' and user_type != 'A' and user_type != 'C':
                    return {'estatus': 403, 'error': 'Usuario sin permisos', 'mensaje': 'Error, usuario sin permisos'}, 403
                
                cui = token['idUsuario']
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
            cur.execute("select * from detalle_carrito d where d.id_usuario = "+str(cui)+" and d.estado = 'P';")
            if cur.rowcount > 0:
                sql = "UPDATE detalle_carrito SET estado = 'C' WHERE estado = 'P' AND id_usuario = "+cui+";"
                cur.execute(sql)
                conn.commit()
            else:
                return jsonify({'estatus': 502, 'error': 'Error del requerimiento', 'mensaje': 'Error, no existen productos actualmente en el carrito'}), 502
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()
        respuesta = {
            "estatus": 200,
            "mensaje": "Compra cancelada exitosamente"
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
    

