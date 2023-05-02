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


@app.route('/compra/registro-externo', methods=['POST'])
def registro_compra_externa():
    try:
        fecha = request.json['fecha']
        productos = request.json['productos']
        auth_header = request.headers.get('Authorization')
        if auth_header: 
            token = auth_header.replace('Bearer ', '')
            token = decode_token(token)
            if 'error' in token:
                # El token es inválido o ha expirado
                return jsonify({'estatus': 401, 'msg': 'Token no válido'}), 401      
            grupo = token['id_grupo']
            seccion = token['seccion']
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
            
            total= 0 
            for producto in productos:
                
                total = total + (float(producto['precio_unitario'])*float(producto['cantidad']))
            
            id = 0
            cur.execute("select id_compra_interna from Compra_interna order by id_compra_interna desc limit 1;")
            if cur.rowcount > 0:
                rows = cur.fetchall()
                for row in rows:
                    id = int(row[0]) + 1
            sql = "INSERT INTO Compra_interna(fecha_venta, numero_grupo, seccion_grupo, total) VALUES(%s,%s, %s, %s)"
            values = (fecha,grupo, seccion, total)
            cur.execute(sql, values)
            # id = cur.fetchone()[0]
            conn.commit()
            for producto in productos:
                sql = "INSERT INTO Detalle_compra_interna(sku,precio,cantidad,id_compra_interna) VALUES(%s,%s,%s,%s);"
                values = (producto['sku'],producto['precio_unitario'],producto['cantidad'],id )
                cur.execute(sql, values)
                conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            return jsonify({'status': 404, 'msg': 'No se encontró el recurso solicitado'}), 404

        finally:
            # Cerrar el cursor y la conexión a la base de datos
            cur.close()
            conn.close()
            
        respuesta = {
            "status": 201,
            "msg": "Transacción realizada con éxito"
        }
        
        return jsonify(respuesta), 201
    
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
    

