import os
import jwt
import bcrypt
import datetime

from .config.dbconnection import db_connection
from flask_expects_json import expects_json
from jsonschema import ValidationError
from .validator import body_model
from flask import Flask, request
from datetime import timezone

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
        'mensaje': "pong"
    }, 200


@app.route(f'{BASE}/login', methods=['POST'])
@expects_json(body_model, check_formats=True)
def login():
    data = request.get_json()
    pass_byte = data['contraseña'].encode()

    try:
        cursor = db_connection()
    except Exception as e:
        return {
            'estatus': 500,
            'error': "No se pudo conectar a la base de datos",
            'mensaje': "Al intentar conectarse a la base de datos hubo un error: " + e.__str__()
        }, 500

    # logic for authentication


@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        err = error.description
        return {
            'estatus': 400,
            'error': 'Parámetros inválidos',
            'mensaje': err.message
        }, 400
    return {
        'estatus': 400,
        'error': "Problema al consultar el servicio",
        'mensaje': error.description
    }, 400
