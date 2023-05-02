import json
import os
import random
import string
import requests

from .config.redisConnection import connection
from flask_expects_json import expects_json
from jsonschema import ValidationError
from .validator import body_model
from flask import Flask, request

env = os.getenv('FLASK_DEBUG', '1')

if env == '1':
    from dotenv import load_dotenv

    load_dotenv(verbose=True)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 100 * 1000
BASE = '/user'

def generate_code():
    list_data = list(string.ascii_letters + string.digits)
    code = [random.choice(list_data) for _ in range(6)]

    return "".join(code)

@app.route(f'{BASE}/ping')
def ping():
    return {
        'estatus': 200,
        'mensaje': 'pong'
    }, 200

@app.route(f'{BASE}/verifyCode', methods=['POST'])
@expects_json(body_model, check_formats=True)
def generatedCode():
    data = request.get_json()
    code = generate_code()

    try:
        redis = connection()
    except Exception as e:
        return {
            'estatus': 500,
            'error': "Error al conectarse a redis",
            'mensaje': "no se pudo establecer la conección con redis " + e.__str__()
        }, 500

    try:
        redis.set('verifyCode', code, ex=5*60)
    except Exception as e:
        return {
            'estatus': 500,
            'error': "No se pudo agregar el elemento",
            'mensaje': "El elemento no fue agregado a redis: " + e.__str__()
        }, 500

    data['data'] = json.dumps({'code': code})

    try:
        res = requests.post(os.getenv('URL_NOTIFICATION'), data)
    except Exception as e:
        return {
            'estatus': 503,
            'error': "Servicio no disponible",
            'mensaje': "El servicio de notificación no se encuentra disponible ahora, por favor intentarlo mas tarde"
        }, 503

    res = res.json()

    if res['estatus']  != 200:
        return {
            'estatus': res['estatus'],
            'error': res['error'],
            'mensaje': res['mensaje']
        }, res['estatus']

    return {
        'estatus': 200,
        'mensaje': "Código de verificación generado exitosamente"
    }, 200

@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        err = error.description,
        return {
            'estatus': 400,
            'error': "Parámetros invalidos",
            'mensaje': err.message
        }, 400

    return {
        'estatus': 400,
        'error': "Problema al consultar el servicio",
        'mensaje': error.description
    }, 400