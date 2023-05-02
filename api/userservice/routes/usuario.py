from flask import Flask, make_response, jsonify
from flask.globals import request
from flask_cors import CORS

# importaciones
import jwt
from datetime import datetime as dt, timedelta
import hashlib
import os

import requests

env = os.getenv('FLASK_DEBUG', '1')
#print("env:", env)
if env == '1':
    from dotenv import load_dotenv
    load_dotenv(verbose=True)

#from db_config import conn
import psycopg2



#host_pagina = "http://localhost:5050"
#url_enviarcorreo = 'http://localhost:6001/notification/sendEmail'
host_pagina = os.getenv('URL_PAGINA')
url_enviarcorreo = os.getenv('URL_NOTIFICATION')


app = Flask(__name__)
CORS(app)

#usuario = Blueprint("user", __name__, url_prefix="/user")
BASE = '/user'

# Conexion a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname = os.getenv('PG_DATABASE'),
    user = os.getenv('PG_USER'),
    password = os.getenv('PG_PASS'),
    host = os.getenv('PG_HOST'),  
    port = os.getenv('PG_PORT')
)

def hash_password(password: str):
    hashed_password = hashlib.md5(password.encode())
    return hashed_password.hexdigest()

@app.route(f'{BASE}/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}

@app.route('/')
def index():
    return 'servier run Flask!'

def create_app():
    return app


@app.route(BASE+'/signin',methods=['POST'])
def addUsuario():
    cur = conn.cursor()
    try:
        cui = request.json['cui']
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        correo = request.json['correo']
        contrasena = request.json['contrasena']
        fecha_nacimiento = request.json.get('fecha_nacimiento')
        tipo = request.json['tipo']
        
        #print("request.json", request.json)

        numero_grupo = None
        seccion_grupo = None
        if tipo == 'E':
            numero_grupo = request.json.get('numero_grupo')
            seccion_grupo = request.json.get('seccion_grupo')

            if numero_grupo == None or seccion_grupo == None:
                return make_response(jsonify(
                    {
                        "estatus": 401,
                        "mensaje": "Si es usuario empresarial debe de ingresar numero de grupo o seccion"
                    }
                ),
                401)

        #print("numero_grupo", numero_grupo)
        #print("seccion_grupo", seccion_grupo)

        #print("hash_password(contrasena):", hash_password(contrasena))

        query = "SELECT cui from usuario where cui = %s"
        cur.execute(query, (cui,))
        if cur.rowcount > 0:
            print("El usuario ya existe en la tabla usuario")
            return jsonify(
                {'estatus': 500, 'error': 'Error interno del servidor', 
                 'mensaje': 'Error, ya existe usuario con el mismo cui. '
                }), 500

        sql = "INSERT INTO usuario(cui, nombres, apellidos, correo, contrasena, fecha_nacimiento, tipo, estado, numero_grupo, seccion_grupo)\
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (cui,nombres, apellidos, correo, hash_password(contrasena), fecha_nacimiento, tipo, 0, numero_grupo, seccion_grupo)
        cur.execute(sql, values)

        # creando enlace para activar cuenta
        exp_time = dt.utcnow()+timedelta(minutes=5)
        encoded = jwt.encode({"cui": cui,"exp": exp_time}, "activar", algorithm="HS256")

        enlace = host_pagina + "/cuenta/confirmar/"+encoded
        print("enlace:", enlace)

        # enviar correo
        url = url_enviarcorreo
        data = {
            'para': correo,
            'asunto': 'CONFIRMAR CUENTA',
            'mensaje': 'bienvenido ' +nombres +" " + apellidos ,
            'plantilla': 'confirmEmail',
            'data': '{"code": "'+enlace+'"}'
        }

        response = requests.post(url, data=data)
        #print("response:", response)
        #print(response.status_code)
        #print(response.content)

        if response.status_code != 200:
            conn.rollback()
            cur.close()
            return {'estatus': 400, 'error':'error',  'mensaje': 'error al enviar correo'}, 400
             

        conn.commit()
        cur.close()
        return make_response(
                jsonify(
                    {
                        "estatus": 200,
                        "mensaje": "Se ha registrado el usuario exitosamente"
                    }
                ),
                200
            )

    except Exception as e:
        conn.rollback()
        cur.close()
        print(e.__str__())
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400


@app.route(BASE+'/login',methods=['POST'])
def login():
    cur = conn.cursor()
    try:
        correo = request.json['correo']
        contrasena = request.json['contrasena']
        #print("request.json", request.json)

        query = "SELECT cui, nombres, apellidos, fecha_nacimiento, tipo, estado, numero_grupo, seccion_grupo\
        from usuario where correo = %s and contrasena = %s"
        cur.execute(query, (correo, hash_password(contrasena)))

        print("cur.rowcount:", cur.rowcount)
        if cur.rowcount == 0:
            return jsonify(
                {'estatus': 404, 'error': 'Falló la autenticación', 
                 'mensaje': 'Error, correo o contraseña no existen'
                }), 404
        
        rows = cur.fetchone()
        #print(rows)
        usuario = {
            "cui":rows[0],
            "nombres":rows[1],
            "apellidos":rows[2],
            "fecha_nacimiento":rows[3],
            "tipo":rows[4],
            "estado":rows[5],
            "numero_grupo":rows[6],
            "seccion_grupo":rows[7]
        }

        if rows[5] != 1: 
             return make_response(
                jsonify(
                    {
                        "estatus": 400,
                        'error': 'Falló la autenticación',
                        "mensaje": "el usuario no esta activo",
                    }
                ),
                400
            )

        cur.close()

        exp_t = dt.utcnow()+timedelta(hours=24)
        encoded = jwt.encode(
             {"cui": rows[0], "id_grupo": rows[6], "seccion": rows[7],"exp": exp_t}, "secret", algorithm="HS256")
        
        return make_response(
                jsonify(
                    {
                        "estatus": 200,
                        "mensaje": "Se inició sesión correctamente",
                        "id_grupo": 914,
                        "seccion": "N",
                        "data": usuario,
                        "token": encoded
                    }
                ),
                200
            )

    except Exception as e:
            conn.rollback()
            cur.close()
            print(e.__str__())
            return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400


@app.route(BASE+'/verifyemail',methods=['POST'])
def verifyemail():
    cur = conn.cursor()

    try:
        token = request.json['token']
        #print("token", token)

        secret_key = 'activar'
        payload = jwt.decode(token, secret_key, algorithms='HS256')
        
        cui = payload['cui']
        #print("cui:", cui)

        query = "SELECT cui, nombres, apellidos, fecha_nacimiento, tipo, estado\
        from usuario where cui = %s"
        cur.execute(query, (cui,))

        #print("cur.rowcount:", cur.rowcount)
        if cur.rowcount == 0:
            return jsonify(
                {'estatus': 404, 'error': 'activacion cuenta', 
                 'mensaje': 'no existe usuario'
                }), 404

        sql = "UPDATE usuario SET estado =  %s WHERE cui = %s"
        cur.execute(sql, (1, cui))
        conn.commit()

        return make_response(
                jsonify(
                    {
                        "estatus": 200,
                        "mensaje": "se activó cuenta correctamente"
                    }
                ),
                200
            )

    except jwt.ExpiredSignatureError:
        cur.close()
        return make_response(
                jsonify(
                    {
                        "estatus": 300,
                        'error': 'JWT ya expiro',
                        "mensaje": "ya expiro invitacion",
                    }
                ),
                300
            )
    except jwt.InvalidTokenError:
        cur.close()
        return make_response(
                jsonify(
                    {
                        "estatus": 400,
                        'error': 'Error en token enviado',
                        "mensaje": "Error en token invalido",
                    }
                ),
                400
            )
        
    except Exception as e:
        conn.rollback()
        cur.close()
        print(e.__str__())
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400
    #cur.close()
    #return {'estatus': 400, 'error':'error',  'mensaje': 'Error al interpretar la solicitud'}, 400

@app.route(BASE+'/profile/<cui>',methods=['GET'])
def profile(cui):
    cur = conn.cursor()

    try:

        #ejemplo para enviar peticion con autorizacion
        """url = "http://localhost:5050/user/verificartoken"

        response = requests.get(url, headers=request.headers)
        res = response.json()
        if response.status_code != 200:
            cur.close()
            print("response.json", response.json())
            return {'estatus': 400, 'error':res['error'],  'mensaje': res['mensaje']}, 400"""
        
        res = decode_token(request)
        #print("res:", res.get_json())
        if res.get_json()['correcto'] != True:
            cur.close()
            return res
        
        query = "SELECT cui, nombres, apellidos, fecha_nacimiento, tipo, estado, numero_grupo, seccion_grupo\
        from usuario where cui = %s"
        cur.execute(query, (cui,))

        if cur.rowcount == 0:
            return jsonify(
                {'estatus': 404, 'error': 'cuenta', 
                 'mensaje': 'no existe usuario'
                }), 404

        rows = cur.fetchone()
        usuario = {
            "cui":rows[0],
            "nombres":rows[1],
            "apellidos":rows[2],
            "fecha_nacimiento":rows[3],
            "tipo":rows[4],
            "estado":rows[5],
            "numero_grupo":rows[6],
            "seccion_grupo":rows[7]
        }

        return make_response(
                jsonify(
                    {
                        "estatus": 200,
                        "mensaje": "correcto",
                        "data": usuario
                    }
                ),
                200
            )
    
    except Exception as e:
        conn.rollback()
        cur.close()
        print(e.__str__())
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400
    

@app.route(BASE+'/verificartoken',methods=['GET'])
def verificartoken():

    res = decode_token(request)
    return res


def decode_token(request):

    try:
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.replace('Bearer ', '')

            secret_key = "secret"
            payload = jwt.decode(token, secret_key, algorithms='HS256')
            return make_response(jsonify({'correcto': True, 'estatus': 200, 'data': payload}), 200)
        else: 
            # No hay un token en la cabecera
            return make_response(jsonify({'correcto': False,'estatus': 401, 'error': 'Usuario no autenticado', 'mensaje': 'Error, usuario no autorizado'}), 401)
            
    except jwt.ExpiredSignatureError:
        return make_response(
                jsonify(
                    {
                        'correcto': False, "estatus": 300,
                        "error": 'Token ha expirado, iniciar sesión de nuevo', 'mensaje': 'Error, con el token'
                    }
                ),
                300
            )

    except jwt.InvalidTokenError:
        return make_response(
                jsonify(
                    {
                        'correcto': False, "estatus": 400,
                        'error': 'Token invalidó, iniciar sesión de nuevo', 'mensaje': 'Error, con el token'
                    }
                ),
                400
            )
    
    except Exception as e:
        print(e.__str__())
        return make_response(jsonify({'correcto': False, 'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}), 400)