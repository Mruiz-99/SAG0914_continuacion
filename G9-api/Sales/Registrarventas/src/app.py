import os
import datetime
from flask import Flask, request,jsonify
from flask_cors import CORS
from . import schema
import jwt
from .db import conn

env = os.getenv('FLASK_ENV', 'development')
if env == 'development':
    from dotenv import load_dotenv
    load_dotenv(verbose=True)


app = Flask(__name__)
CORS(app)
baserUrl = '/sales'


@app.route( f'{baserUrl}/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong Servicio de billetera '}


# parametros
# cui
@app.route(f'{baserUrl}/getsales', methods=['GET'])
def recordSales():
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(" ")[1]
            decoded_token = decode_token(token)
            if 'error' in decoded_token:
                # El token es inválido o ha expirado
                return jsonify({'estatus': 401, 'error': decoded_token['error'], 'mensaje': decoded_token['mensaje']}), 401
        else:
            # No hay un token en la cabecera
            return jsonify({'estatus': 401, 'error': 'Usuario no autenticado', 'mensaje': 'Error, usuario no autorizado'}), 401
      
        # Se crea un cursor para ejecutar consultas SQL
        cur = conn.cursor()
        stmSelect = """ SELECT dc.id_detalle_carrito, dc.cantidad, dc.id_usuario, u.nombres, dc.estado, 
                        p.nombre,dc.id_ruta, dc.id_producto, sum(dc.cantidad * p.precio_unitario) as precio_total, 
                        r.nombre AS nombre_ruta
                        FROM detalle_carrito dc
                        INNER JOIN producto p ON dc.id_producto = p.sku 
                        INNER JOIN usuario u ON dc.id_usuario = u.cui 
                        LEFT JOIN ruta r ON dc.id_ruta = r.id_ruta 
                        WHERE dc.estado = 'P'
                        GROUP BY dc.id_detalle_carrito, dc.cantidad, dc.id_usuario, u.nombres, dc.estado, 
                                p.nombre,dc.id_ruta, dc.id_producto, r.nombre;
                    """
        cur.execute(stmSelect)
        conn.commit()
        # procesar el resultado
        data = []
        for row in cur.fetchall():
            # Verificar si ya existe el usuario en el diccionario
            user_exists = False
            for user_data in data:
                if user_data["id_usuario"] == row[2]:
                    user_exists = True
                    # Agregar el producto al usuario existente
                    user_data["total"] = user_data["total"] + row[8]
                    product_data = {
                        "id_detalle_carrito": row[0],
                        "cantidad": row[1],
                        "nombre": row[5],
                        "id_ruta": row[6],
                        "id_producto": row[7],
                        "precio_total": row[8],
                    }
                    user_data["productos"].append(product_data)
                    break
            # Si el usuario no existe en el diccionario, agregarlo
            if not user_exists:
                user_data = {
                        "id_usuario": row[2],
                        "nombre": row[3],
                        "estado": row[4],
                        "nombre_ruta": row[9],
                        "total": row[8],
                        "productos": [{
                            "id_detalle_carrito": row[0],
                            "cantidad": row[1],
                            "nombre": row[5],
                            "id_ruta": row[6],
                            "id_producto": row[7],
                            "precio_total": row[8],
                        }]
                    }
                data.append(user_data)

        # Cierre de la conexión y el cursor
        #cur.close()
        #conn.close()
        return jsonify({'estatus':200, 'mensaje': 'Ventas encontradas', 'data':data }), 200

    except Exception as e:
        print(e)
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al registrar venta'}, 400

def decode_token(token):
    try:
        secret_key = os.getenv('JWT_KEY')
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}

    except jwt.InvalidTokenError:
        return {'error': 'Token invalidó, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}



