# importaciones
from flask import Flask, make_response, jsonify, Blueprint
from db_config import mydb
from mysql.connector import Error
from flask.globals import request
import jwt
from datetime import datetime as dt, timedelta

usuario = Blueprint("usuario", __name__, url_prefix="/usuario")


data_usuario = []
meth = ['GET', 'POST', 'DELETE', 'PUT']


@usuario.route('/addUsuario', methods=meth)
def addUsuario():

    mycursor = mydb.cursor()
    query = "INSERT INTO Usuario (cui, nombres, apellidos, contra, correo, tipo, estado, id_grupo, seccion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    try:
        if request.method == 'POST':
            error = False
            # datos que se necesitan para login
            cui = request.json['cui']
            nombres = request.json['nombres']
            apellidos = request.json['apellidos']
            contra = request.json['contra']
            correo = request.json['correo']
            tipo = request.json['tipo']
            estado = request.json['estado']
            id_grupo = request.json['id_grupo']
            seccion = request.json['seccion']

            res = mycursor.execute(
                query, (cui, nombres, apellidos, contra, correo, tipo, estado, id_grupo, seccion))
            mydb.commit()

            mycursor.close()
            if error == False:
                return make_response(
                    jsonify(
                        {
                            "status": 200,
                            "Mensaje": 'usuario ' + cui + ' correctamente registrado'
                        }
                    ),
                    200
                )
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "Mensaje": 'Ha ocurrido un error al ingreso del usuario'
                    }
                ),
                400
            )
        else:
            retorno = {'mensaje': 'Este método no se maneja'}
        return jsonify(retorno)
    except Error as e:
        return make_response(
            jsonify(
                {
                    "status": 500,
                    "Mensaje": f"Error interno en el servidor: {e}"
                }
            ),
            500
        )


@usuario.route('/editUsuario', methods=meth)
def editUsuario():
    print(request.method)
    if request.method == 'PUT':
        error = False
        # datos que se necesitan para login
        cui = request.json['cui']
        correo = request.json['correo']

        id = 0
        if len(data_usuario) == 0:
            id = 1
        else:
            libro = data_usuario[len(data_usuario) - 1]
            id = libro['id'] + 1

        data_res = {
            'id': id,
            'cui': cui,
            'correo': correo
        }
        data_usuario.append(data_res)
        if error == False:
            return make_response(
                jsonify(
                    {
                        "status": 200,
                        "Mensaje": 'Se han actualizado los datos del usuario ' + cui
                    }
                ),
                200
            )
        return make_response(
            jsonify(
                {
                    "status": 400,
                    "Mensaje": 'Ha ocurrido un error en la actualización de datos'
                }
            ),
            400
        )
    else:
        retorno = {'mensaje': 'Este método no se maneja'}
    return jsonify(retorno)


@usuario.route('/infoUsuario/<cui>', methods=meth)
def getUsuario(cui):
    try:
        mycursor = mydb.cursor()
        query = "SELECT * FROM Usuario WHERE cui = %s"

        if request.method == 'POST':
            error = False
            mycursor.execute(query, (cui,))
            if error == False:
                return make_response(
                    jsonify(
                        {
                            "status": 200,
                            "Mensaje": 'datos obtenidos'
                        }
                    ),
                    200
                )
            return make_response(
                jsonify(
                    {
                        "status": 400,
                        "Mensaje": 'Ha ocurrido un error al ingreso del usuario'
                    }
                ),
                400
            )

        else:
            retorno = {'mensaje': 'Este método no se maneja'}
        return jsonify(retorno)
    except Error as e:
        return make_response(
            jsonify(
                {
                    "status": 500,
                    "Mensaje": f"Error interno en el servidor: {e}"
                }
            ),
            500
        )
