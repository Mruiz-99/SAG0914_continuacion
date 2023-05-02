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

def create_app():
    return app

@app.route('/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}


@app.route('/buy/addShoppingCart', methods=['POST'])
def agregar_producto_carrito():
    form = validators.AgregarProductoCarrito(request.form)
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
                if user_type != 'E' and user_type != 'A' and user_type != 'C':
                    return {'estatus': 403, 'error': 'Usuario sin permisos', 'mensaje': 'Error, usuario sin permisos'}, 403
                
                cui = token['idUsuario']
                if form.cantidad.data == None:
                    cantidad = 1
                else:
                    cantidad = form.cantidad.data
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
   
            # Si existe un carrito creado en estado de pendiente
            sql = "INSERT INTO detalle_carrito(cantidad, id_usuario, estado, id_producto, id_ruta) VALUES (%s,%s, %s, %s, %s)"
            values = (cantidad,cui, 'P',form.id_producto.data, None)
            cur.execute(sql, values)
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()
        respuesta = {
            "estatus": 200,
            "mensaje": "Producto agregado correctamente"
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
    

