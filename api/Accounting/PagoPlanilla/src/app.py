import io
import os
from flask import Flask, request,jsonify
from . import schema
import jwt

env = os.getenv('FLASK_ENV', 'development')
if env == 'development':
    from dotenv import load_dotenv
    load_dotenv(verbose=True)


app = Flask(__name__)
baserUrl = '/accounting'


@app.route( f'{baserUrl}/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong Pago de planilla '}


@app.route(f'{baserUrl}/payroll', methods=['POST'])
@schema.validate_schema()
def addAuthor():
    try:
        
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            
            token = auth_header.split(" ")[1]
            decoded_token = decode_token(token)
            if 'error' in decoded_token:
                # El token es inválido o ha expirado
                return jsonify({'estatus': 401, 'error': decoded_token['error'], 'mensaje': decoded_token['mensaje']}), 401
            else:
                
                # verificar si el usuario es admin
                user_type = decoded_token['tipoUsuario']
                if user_type != 1:
                    return {'estatus': 403, 'error': 'Usuario sin permisos', 'mensaje': 'Error, usuario sin permisos'}, 403
        else:
            # No hay un token en la cabecera
            return jsonify({'estatus': 401, 'error': 'Usuario no autenticado', 'mensaje': 'Error, usuario no autorizado'}), 401
       
        print('Registrando planilla')
        cui = request.json.get('cui')
        metodo = request.json.get('metodo')
        mes = request.json.get('mes')
        anio = request.json.get('anio')
        moneda = request.json.get('moneda')
        descripcion = request.json.get('descripcion')
        print(cui, metodo, mes, anio, moneda, descripcion)
        
        retornar = {
                'estatus': 201,
                'mensaje': 'Se ha registrado la planilla  correctamente',
                'data':jsonreturn
        }
        return (jsonify(retornar), 201)

    except Exception as e:
        print(e)
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al Registrar planilla'}, 400

def decode_token(token):
    try:
        secret_key = os.getenv('JWT_KEY')
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {'error': 'Token ha expirado, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}

    except jwt.InvalidTokenError:
        return {'error': 'Token invalidó, iniciar sesión de nueva', 'mensaje': 'Error, con el token'}

jsonreturn = {
    "nombreEmpresa": "ACME Corporation",
    "mes": "Diciembre",
    "año": 2023,
    "empleado": {
      "nombre": "Juan Pérez",
      "cui": "1234567890123",
      "puesto": "desarrollador frontend",
      "tipoPago": "transferencia bancaria",
      "sueldoBase": 5000,
      "bonificacion": [
        {
          "tipo": "productividad",
          "monto": 1000.0
        },
        {
          "tipo": "asistencia",
          "monto": 500.0
        }
      ],
      "extras": [
        {
          "tipo": "capacitación",
          "descripcion": "Curso de ventas"
        },
        {
          "tipo": "proyecto especial",
          "descripcion": "Desarrollo de una nueva aplicación"
        }
      ],
      "retencion": [
        {
          "tipo": "impuestos",
          "monto": 800.0
        },
        {
          "tipo": "préstamos",
          "monto": 300.0
        }
      ],
      "total": 8000
    }
  }
