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
# idUsuario
# total
# -- estado de pago: 0: pendiente, 1: pagado, 2: rechazado
# tipoPago  -- 0: tarjeta, 1: wallet , 2: mixto

# -- estado de pago: 0: pendiente, 1: pagado, 2: rechazado
@app.route(f'{baserUrl}/acceptpayment', methods=['POST'])
@schema.validate_schema()
def acceptpayment():
    try:
        print("acceptpayment")
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
        # obtener el pago
        stmSelect = "select * from pago where id_usuario = %s and estadopago=0;"
        values = (request.json.get('id_usuario'),)
        cur.execute(stmSelect, values)
        pago = cur.rowcount
        # verificar el pago
        if pago != 0:
            # tipo de pag
            # pago con wallet
            infoPago = cur.fetchone()
            if(infoPago[6]==1):
                # verificar que el total sea menor o igual al monto de la billetera
                stmSelectwallet = "select * from billetera where id_usuario = %s;"
                values2 = (request.json.get('id_usuario'),)
                cur.execute(stmSelectwallet, values2)
                montoBilletera = cur.fetchone()[2]
                if(montoBilletera >= request.json.get('total')):
                    # actualizar el monto de la billetera
                    montoBilletera = montoBilletera - request.json.get('total')
                    stmUpdate = "update billetera set monto = %s where id_usuario = %s;"
                    values3 = (montoBilletera,request.json.get('id_usuario'),)
                    cur.execute(stmUpdate, values3)
                    conn.commit()
                    # actualizar el estado del pago
                    stmUpdate = "update pago set estadopago = %s where id_usuario = %s;"
                    values = (1,request.json.get('id_usuario'),)
                    cur.execute(stmUpdate, values)
                    conn.commit()
                    return jsonify({'estatus': 200, 'mensaje': 'Pago registrado exitosamente. ' }), 200
                else:
                    return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Saldo insuficiente en la billetera'}), 500
            elif (infoPago[6]==2):
                #mixto
                # verificar que el total sea menor o igual al monto de la billetera
                stmSelectwallet = "select * from billetera where id_usuario = %s;"
                values2 = (request.json.get('id_usuario'),)
                cur.execute(stmSelectwallet, values2)
                aux = cur.fetchone()
                montoBilletera = aux[2]

                montoBilleteraPago =infoPago[1]
                # verificar que el monto de pago sea menor o igual al monto de la billetera
                if(montoBilletera >= montoBilleteraPago):
                    # actualizar el monto de la billetera
                    montoBilletera = montoBilletera - montoBilleteraPago
                    stmUpdate = "update billetera set monto = %s where id_usuario = %s;"
                    values3 = (montoBilletera,request.json.get('id_usuario'),)
                    cur.execute(stmUpdate, values3)
                    conn.commit()
                    # actualizar el estado del pago
                    stmUpdate = "update pago set estadopago = %s where id_usuario = %s;"
                    values = (1,request.json.get('id_usuario'),)
                    cur.execute(stmUpdate, values)
                    conn.commit()
                    return jsonify({'estatus': 200, 'mensaje': 'Pago registrado exitosamente. ' }), 200
                else:
                    return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Saldo insuficiente en la billetera'}), 500            
            return jsonify({'estatus': 200, 'mensaje': 'Pago registrado exitosamente. ' }), 200
            
        else :
            return jsonify({'estatus': 500, 'error': 'Error interno del servidor', 'mensaje': 'Error en la base de datos, registro de pago no encontrado'}), 500

    except Exception as e:
        print("error accept payment", e)
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al confirmar pago'}, 400

def decode_token(token):
    try:
        secret_key = os.getenv('JWT_KEY')
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}

    except jwt.InvalidTokenError:
        return {'error': 'Token invalidó, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}



