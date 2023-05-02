from flask import Flask, make_response,jsonify, Blueprint
from db_config import mydb
from mysql.connector import Error
from flask.globals import request

pago = Blueprint("pago", __name__, url_prefix="/pago")

# agregar tarjeta
@pago.route("/addtarjeta",methods=['POST'])
def addtarjeta():

    mycursor = mydb.cursor()
    query = "INSERT INTO tarjeta (iduser, cuenta, saldo)\
    VALUES (%s, %s, %s)"

    try:
        iduser = request.json['iduser']
        cuenta = request.json['cuenta']
        saldo = 0.00


        res = mycursor.execute(query, (iduser, cuenta, saldo))
        mydb.commit()

        mycursor.close()
        #mydb.close()
        print("res", res)
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje" : 'se registró correctamente'
                        }
                    ),
                    200
            )
    except Error as e:
        return make_response(
                jsonify(
                    {
                    "status" : 500,
                    "Mensaje" : f"Error interno en el servidor: {e}"
                    }
                ),
                500
        )

# agregar cartera
@pago.route("/addcartera",methods=['POST'])
def addcartera():

    mycursor = mydb.cursor()
    query = "INSERT INTO cartera (iduser, cuenta, saldo)\
    VALUES (%s, %s, %s)"

    try:
        iduser = request.json['iduser']
        cuenta = request.json['cuenta']
        saldo = 0.00


        res = mycursor.execute(query, (iduser, cuenta, saldo))
        mydb.commit()

        mycursor.close()
        #mydb.close()
        print("res", res)
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje" : 'se registró cartera correctamente'
                        }
                    ),
                    200
            )
    except Error as e:
        return make_response(
                jsonify(
                    {
                    "status" : 500,
                    "Mensaje" : f"Error cartera interno en el servidor: {e}"
                    }
                ),
                500
        )

# get all tarjetas
@pago.route("/gettarjetas/<iduser>",methods=['GET'])
def gettarjetas(iduser):

    mycursor = mydb.cursor()
    query = "SELECT idtarjeta, iduser, cuenta, saldo\
        FROM tarjeta WHERE iduser = %s"

    mycursor.execute(query, (iduser,))

    data = []
    for row in mycursor.fetchall():
        row_act = {
            "idtarjeta":row[0],
            "iduser":row[1],
            "cuenta":row[2],
            "saldo":row[3]
        }
        data.append(row_act)

    #print("data: ", data)
    return make_response(
                jsonify(
                    {
                    "status" : 200,
                    "Mensaje":"datos obtenidos",
                    "data":data
                    }
                ),
                200
        )

# get all carteras
@pago.route("/getcarteras/<iduser>",methods=['GET'])
def getcarteras(iduser):

    mycursor = mydb.cursor()
    query = "SELECT idcartera, iduser, cuenta, saldo\
        FROM cartera WHERE iduser = %s"

    mycursor.execute(query, (iduser,))

    data = []
    for row in mycursor.fetchall():
        row_act = {
            "idcartera":row[0],
            "iduser":row[1],
            "cuenta":row[2],
            "saldo":row[3]
        }
        data.append(row_act)

    #print("data: ", data)
    return make_response(
                jsonify(
                    {
                    "status" : 200,
                    "Mensaje":"datos obtenidos",
                    "data":data
                    }
                ),
                200
        )


# agregar monto cartera
@pago.route("/addmonto",methods=['POST'])
def addmonto():

    mycursor = mydb.cursor()
    query = "UPDATE cartera SET saldo = saldo + %s\
    WHERE idcartera = %s"

    try:
        idcartera = request.json['idcartera']
        monto = request.json['monto']

        res = mycursor.execute(query, (monto, idcartera))
        mydb.commit()

        mycursor.close()
        #mydb.close()
        #print("res", res)
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje" : 'se registró monto a cartera correctamente'
                        }
                    ),
                    200
            )
    except Error as e:
        return make_response(
                jsonify(
                    {
                    "status" : 500,
                    "Mensaje" : f"Error cartera interno en el servidor: {e}"
                    }
                ),
                500
        )
    
# pagar
@pago.route("/addpago",methods=['POST'])
def addpago():

    mycursor = mydb.cursor()
    query = "INSERT INTO pagos (iduser, idtarjeta, idcartera, idcompra, idventa, monto)\
    VALUES (%s, %s, %s, %s, %s, %s)"

    query_car = "UPDATE cartera SET saldo = saldo - %s\
    WHERE idcartera = %s"

    try:
        iduser = request.json['iduser']
        idtarjeta = request.json['idtarjeta']
        idcartera = request.json['idcartera']
        idcompra = request.json['idcompra']
        idventa = request.json['idventa']
        monto = request.json['monto']


        res = mycursor.execute(query, (iduser, idtarjeta, idcartera, idcompra, idventa, monto))
        
        #print("idcartera:", idcartera)
        if idcartera != None:
            res_c = mycursor.execute(query_car, (monto, idcartera))
        
        mydb.commit()
        mycursor.close()
        #mydb.close()
        #print("res", res)
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje" : 'se realizó el pago correctamente'
                        }
                    ),
                    200
            )
    except Error as e:
        return make_response(
                jsonify(
                    {
                    "status" : 500,
                    "Mensaje" : f"Error interno en el servidor: {e}"
                    }
                ),
                500
        )


# validar monto cartera
@pago.route("/valmontopago",methods=['POST'])
def valmontopago():
    mycursor = mydb.cursor()
    query = "SELECT iduser, cuenta, saldo FROM cartera\
    WHERE idcartera = %s"

    try:
        idcartera = request.json['idcartera']
        monto = request.json['monto']

        mycursor.execute(query, (idcartera,))
        myresult = mycursor.fetchone()

        producto = {}
        if not myresult is None:
            producto = {
                "iduser":myresult[0],
                "cuenta":myresult[1],
                "saldo":myresult[2]
            }
        
        print("producto.saldo: ", producto['saldo'])
        print("monto: ", monto, 100)
        if producto['saldo'] < monto:
            return make_response(
                    jsonify(
                        {
                        "status" : 500,
                        "Mensaje" : 'Saldo insuficiente'
                        }
                    ),
                    500
            )
        else:
            return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje" : 'Saldo correcto'
                        }
                    ),
                    200
            )


    except Error as e:
        return make_response(
                jsonify(
                    {
                    "status" : 500,
                    "Mensaje" : f"Error interno en el servidor: {e}"
                    }
                ),
                500
        )