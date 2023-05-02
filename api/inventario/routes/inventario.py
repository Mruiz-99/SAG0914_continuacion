from flask import Flask, make_response, jsonify
from flask.globals import request
from flask_cors import CORS
#from routes.inventario import inventario
# importaciones
#from flask import Flask, make_response, jsonify, Blueprint
#from flask.globals import request
import jwt
from datetime import datetime as dt, timedelta
import hashlib
import os
import io

from . import validators
import requests

env = os.getenv('FLASK_DEBUG', '1')

if env == '1':
    from dotenv import load_dotenv
    load_dotenv(verbose=True)

from db_config import conn

app = Flask(__name__)
CORS(app)
BASE = '/inventario'
#inventario = Blueprint("inventario", __name__, url_prefix="/inventario")

@app.route(BASE+'/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}

@app.route(BASE+'/addproducto',methods=['POST'])
def addproducto():

    #print("request.form:", request.form)
    form = validators.agregarProducto(request.form)
    if not form.validate():
        return {'estatus': 400, 'error': form.errors, 'mensaje': 'Error con los campos.'}, 400
    
    cur = conn.cursor()

    try:
        #print("request.files:", request.files)
        #files_p = request.files.getlist('archivo')
        #files_p = request.files['archivo'].read()
        #print("request.files['archivo']:", request.files['archivo'].filename)


        # extrar el archivo del form-data
        file = request.files['archivo']
        f = io.BytesIO(file.stream.read())
        f.name = file.filename

        # construccion de la info a enviar  
        upload_file = {'archivo': f}

        # request
        #requests.post(os.getenv('URL_UPLOAD'), data={'directorio': '/perfil'}, files=upload_file)

        url = os.getenv('URL_UPLOAD')
        #response = requests.post(url, data={'directorio': '/producto'}, files=upload_file)
        response = requests.post(url, files=upload_file)
        #response = requests.post(url, headers=request.headers, files=upload_file)
        res = response.json()
        if response.status_code != 200:
            cur.close()
            print("response.json", response.json())
            return {'estatus': 400, 'error':res['error'],  'mensaje': res['mensaje']}, 400
        
        dir_ima = res['data'][0]
        print("dir_ima:", dir_ima)
        
        sql = "INSERT INTO producto(sku, nombre, descripcion, precio_costo, imagen, unidades_disponibles, precio_unitario, id_categoria)\
            VALUES (%s, %s,%s, %s, %s, %s, %s, %s)"
        values = (form.sku.data, form.nombre.data,form.descripcion.data, form.precio_costo.data, dir_ima, form.unidades_disponibles.data, form.precio_unitario.data, form.id_categoria.data)
        cur.execute(sql, values)

        conn.commit()
        cur.close()
        return make_response(
                jsonify(
                    {
                        "estatus": 200,
                        "mensaje": "Se ha registrado el producto exitosamente"
                    }
                ),
                200
            )

    except Exception as e:
        conn.rollback()
        cur.close()
        print(e.__str__())
        return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400
    

def create_app():
    return app

# get all producto
@app.route(BASE+"/getproductos",methods=['GET'])
def getproductos():


    query = "SELECT sku, nombre, descripcion, precio_costo, imagen, unidades_disponibles, precio_unitario, id_categoria\
        FROM producto"
    cur = conn.cursor()
    try:
        cur.execute(query, ())

        data = []
        for row in cur.fetchall():
            row_act = {
                "sku":row[0],
                "nombre":row[1],
                "descripcion":row[2],
                "precio_costo":row[3],
                "imagen":row[4],
                "unidades_disponibles":row[5],
                "precio_unitario":row[6],
                "id_categoria":row[7]
            }
            data.append(row_act)

        return make_response(
                jsonify(
                    {
                    "estatus" : 200,
                    "mensaje":"datos obtenidos",
                    "data":data
                    }
                ),
                200
        )

    except Exception as e:
            conn.rollback()
            cur.close()
            print(e.__str__())
            return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400
    

# get all categorias
@app.route(BASE+"/getcategorias",methods=['GET'])
def getcategorias():


    query = "SELECT id_categoria, nombre\
        FROM categoria"
    cur = conn.cursor()
    try:
        cur.execute(query, ())

        data = []
        for row in cur.fetchall():
            row_act = {
                "id_categoria":row[0],
                "nombre":row[1]
            }
            data.append(row_act)

        return make_response(
                jsonify(
                    {
                    "estatus" : 200,
                    "mensaje":"datos obtenidos",
                    "data":data
                    }
                ),
                200
        )

    except Exception as e:
            conn.rollback()
            cur.close()
            print(e.__str__())
            return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400
    

@app.route(BASE+"/getstock/<sku>",methods=['GET'])
def getstock(sku):

    query = "SELECT unidades_disponibles\
        FROM producto WHERE sku = %s"
    cur = conn.cursor()
    try:
        cur.execute(query, (sku,))

        rows = cur.fetchone()
        return make_response(
                jsonify(
                    {
                    "estatus" : 200,
                    "mensaje":"datos obtenidos",
                    "unidades_disponibles":rows[0]
                    }
                ),
                200
        )

    except Exception as e:
            conn.rollback()
            cur.close()
            print(e.__str__())
            return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400
    

@app.route(BASE+"/actualizarstock",methods=['PUT'])
def actualizarstock():
    
    query_suma = "UPDATE producto SET unidades_disponibles = unidades_disponibles + %s\
    WHERE sku = %s"
    query_resta = "UPDATE producto SET unidades_disponibles = unidades_disponibles - %s\
    WHERE sku = %s"

    cur = conn.cursor()
    try:

        sku = request.json['sku']
        unidades = request.json['unidades']
        tipo = request.json['tipo']

        if tipo == "+":
            cur.execute(query_suma, (unidades, sku,))
        elif tipo == "-":
            cur.execute(query_resta, (unidades, sku,))

        conn.commit()
        cur.close()
        return make_response(
                jsonify(
                    {
                        "estatus": 200,
                        "mensaje": "Se ha actualizaron las unidades correctamente"
                    }
                ),
                200
            )

    except Exception as e:
            conn.rollback()
            cur.close()
            print(e.__str__())
            return {'estatus': 400, 'error':e.__str__(),  'mensaje': 'Error al interpretar la solicitud'}, 400