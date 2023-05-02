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
baserUrl = '/payments'


@app.route( f'{baserUrl}/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong Microservicio Registrar Pago '}


# ------- parametros -------
# montoWallet
# montoTarjeta
# idTarjeta
# idBilletera
# idDetalleCarrito
# tipoPago  -- 0: tarjeta, 1: wallet , 2: mixto

# -- estado de pago: 0: pendiente, 1: pagado, 2: rechazado
@app.route(f'{baserUrl}/recordpayment', methods=['POST'])
@schema.validate_schema()
def rechargeWallet():
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
        stmInsert = "insert into pago (montowallet, id_usuario, id_billetera, id_tarjeta, montotarjeta, tipopago,estadopago) VALUES (%s,%s,%s,%s,%s,%s,%s);"
        values = (request.json.get('montowallet'), request.json.get('id_usuario'), request.json.get('id_billetera'), request.json.get('id_tarjeta'), request.json.get('montotarjeta'), request.json.get('tipopago'),0)
        cur.execute(stmInsert, values)
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos'}), 500
        else:
            return jsonify({'estatus': 200, 'mensaje': 'Pago registrado exitosamente. ' }), 200
      

    except Exception as e:
        print(e)
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al crear billetera'}, 400

def decode_token(token):
    try:
        secret_key = os.getenv('JWT_KEY')
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}

    except jwt.InvalidTokenError:
        return {'error': 'Token invalidó, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}



