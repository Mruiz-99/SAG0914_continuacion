import os

from .config.redisConnection import connection
from .config.dbConnection import db_connection
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

@app.route(f'{BASE}/ping')
def ping():
    return {
        'estatus': 200,
        'mensaje': 'pong'
    }, 200


@app.route(f'{BASE}/verifyEmail', methods=['POST'])
@expects_json(body_model, check_formats=True)
def verifyEmail():
    correo = request.get_json()['correo']
    code = request.get_json()['codigoVerificacion']

    try:
        redis = connection()
    except Exception as e:
        return {
            'estatus': 500,
            'error': "Error al conectarse a redis",
            'mensaje': "No se pudo establecer conección con redis " + e.__str__()
        }, 500

    try:
        originCode = redis.get('verifyCode').decode('utf-8')
    except Exception as e:
        return {
            'estatus': 500,
            'error': "Error al obtener el elemento",
            'mensaje': "No se pudo obtener el elemento " + e.__str__()
        }, 500

    if code == originCode:
        # habailable user in system in DB
        try:
            cursor = db_connection()
        except Exception as e:
            return {
                'estatus': 500,
                'error': "No se pudo conectar a la base de datos",
                'mensaje': "Al intentar conectarse a la base de datos hubo un error: " + e.__str__()
            }, 500

        # modify User

        try:
            redis.delete('verifyCode')
        except Exception as e:
            return {
                'estatus': 500,
                'error': "Error al eliminar el item",
                'mensaje': "No se pudo eliminar el item de la base de datos " + e.__str__()
            }, 500

        return {
            'estatus': 200,
            'mensaje': "El correo fue verificado exitosamente"
        }, 200

    return {
        'estatus': 400,
        'error': "Código invalido",
        'mensaje': "El código de verificación es incorrecto o ya expiro"
    }, 400


@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        err = error.description
        return {
            'estatus': 400,
            'error': 'Parámetros invalidos',
            'mensaje': err.message
        }, 400

    return {
        'estatus': 400,
        'error': "Problema al consultar el servicio",
        'mensaje': error.description
    }, 400