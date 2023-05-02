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


@app.route('/inventario/recepcion', methods=['PUT'])
def recepcion_productos_externos():
    try:
        productos = request.json['productos']
        auth_header = request.headers.get('Authorization')
        if auth_header: 
            token = auth_header.replace('Bearer ', '')
            token = decode_token(token)
            
            if 'error' in token:
                # El token es inválido o ha expirado
                return jsonify({'estatus': 401, 'msg': 'Token no válido'}), 401      
        else:
            # No hay un token en la cabecera
            return jsonify({'estatus': 401, 'mgs': 'Token no válido'}), 401
        
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
            for producto in productos:
                sql = "UPDATE Producto SET unidades_disponibles = unidades_disponibles + %s WHERE sku = %s;"

                values = (producto['cantidad'],producto['sku'] )
                cur.execute(sql, values)
                conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'status': 404, 'msg': 'No se encontró el recurso solicitado'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()
            
        respuesta = {
            "status": 200,
            "msg": "Stock del producto actualizado"
        }
        
        return jsonify(respuesta), 200
    
    except Exception as e:
        print(e)
        return {'status': 400, 'msg':'Formato invalido'}, 400
    

def decode_token(token):
    try:
        secret_key = os.getenv('JWT_KEY')
        payload = jwt.decode(token, secret_key, algorithms='HS256')
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado, iniciar sesión de nuevo', 'mensaje': 'Error, con el token'}

    except jwt.InvalidTokenError:
        return {'error': 'Token invalidó, iniciar sesión de nuevo', 'mensaje': 'Error, con el token'}
    

