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


@app.route('/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}


@app.route('/buy/getShoppingCart', methods=['GET'])
def ver_carrito_compra():
    try:
        cui = ''
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
            productos = [{}]
            cur.execute("select p.nombre, p.descripcion, p.imagen, p.precio_unitario, p.unidades_disponibles, c.nombre from detalle_carrito d inner join Producto p on d.id_producto = p.sku inner join Categoria c on c.id_categoria = p.id_categoria where d.id_usuario = "+cui+"and d.estado = 'P';")
            if cur.rowcount > 0:
                rows = cur.fetchall()
                
                for row in rows:
                    producto = {'nombre':row[0],'descripcion':row[1],'imagen':row[2],'precio_unitario':row[3],'unidades_disponibles':row[4],'categoria':row[5]}
                    if productos == [{}]:
                        productos = [producto]
                    else:
                        productos.append(producto)
        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()
        respuesta = {
            "estatus": 200,
            "mensaje": "Productos del carrito de compras",
            "data": productos
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
    

