import os
import datetime
import requests
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
@app.route(f'{baserUrl}/approvesale', methods=['POST'])
@schema.validate_schema()
def approvesale():
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
        # se realiza el pago
        
        # try:
        #     print(request.json.get('cui'))
        #     print(request.json.get('total'))
        #     res = requests.post(os.getenv('URL_CONFIRMARPAGO'), 
        #     data={'id_usuario':request.json.get('cui'),'total':request.json.get('total')}, 
        #     headers={'Authorization': auth_header})
        #     print("res: ",res)
        # except Exception as e:
        #     print("debbug1")
        #     print(e.__str__())
        #     return jsonify({
        #             'estatus': 500,
        #             'error': "Error al confirmar pago ",
        #             'mensaje': "Ocurrio un errro al confirmar el pago " + e.__str__()
        #         }), 500
            
        # res = res.json()
        # if res['estatus'] != 200:
        #     return jsonify({
        #         'estatus': res['estatus'],
        #         'error': res['mensaje'],
        #         'mensaje': res['error']
        #     }), res['estatus']


        stmUpdtadeCarrito = "UPDATE detalle_carrito SET estado = 'C' WHERE id_usuario = %s AND estado = 'P';"
        print(request.json.get('cui'))
        values = (request.json.get('cui'),)
        cur.execute(stmUpdtadeCarrito, values)
        conn.commit()
        # procesar el resultado
        if cur.rowcount == 0:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error al aprobar venta, intnte mas tarde'}), 500
        else:
            return jsonify({'estatus': 200, 'mensaje': 'Venta aprobada con exito.' }), 200

    except Exception as e:
        print(e)
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al aprobar venta, intnte mas tarde'}, 400

def decode_token(token):
    try:
        secret_key = os.getenv('JWT_KEY')
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}

    except jwt.InvalidTokenError:
        return {'error': 'Token invalidó, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}



