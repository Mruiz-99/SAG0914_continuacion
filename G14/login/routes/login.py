# importaciones
from flask import Flask, make_response, jsonify, Blueprint
from flask.globals import request
import jwt
from db_config import mydb
from mysql.connector import Error
from datetime import datetime as dt, timedelta

login = Blueprint("login", __name__, url_prefix="/login")


# login donde generamos el jwt


@login.route('/autentication', methods=['POST'])
def localizacion():
    try:
        print('0')
        mycursor = mydb.cursor()

        query = "SELECT cui, contra FROM Usuario WHERE cui = %s AND contra =%s"

        if request.method == 'POST':
            error = False

            print('hola?')
            # datos que se necesitan para login
            cui = request.json['cui']
            contra = request.json['contra']
            res = mycursor.execute(query, (cui, contra))
            mydb.commit()

            mycursor.close()
            print('hola')
            prueba = dt.utcnow()+timedelta(minutes=2)
            encoded = jwt.encode(
                {"cui": cui, "exp": prueba}, "secret", algorithm="HS256")
            retorno = {'token': encoded, "status": 200}
            if error == False:
                return make_response(
                    jsonify(
                        {
                            "status": 200,
                            "token": retorno
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
