from flask import Flask, make_response,jsonify, Blueprint
from db_config import mydb
from mysql.connector import Error
from flask.globals import request

inventario = Blueprint("inventario", __name__, url_prefix="/inventario")

# agregar producto
@inventario.route("/addproducto",methods=['POST'])
def addproducto():

    mycursor = mydb.cursor()
    query = "INSERT INTO producto (nombre, precio, costo, stock, idcategoria)\
    VALUES (%s, %s, %s, %s, %s)"

    try:
        nombre = request.json['nombre']
        precio = request.json['precio']
        costo = request.json['costo']
        stock = request.json['stock']
        idcategoria = request.json['idcategoria']


        res = mycursor.execute(query, (nombre, precio, costo, stock, idcategoria))
        mydb.commit()

        mycursor.close()
        #mydb.close()
        print("res", res)
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje" : 'se actualizó registro correctamente'
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

# get producto stock
@inventario.route("/getstock/<sku>",methods=['GET'])
def getstock(sku):

    #print("sku", sku, type(sku))
    mycursor = mydb.cursor()
    query = "SELECT stock FROM producto\
    WHERE sku = %s"

    mycursor.execute(query, (sku,))

    myresult = mycursor.fetchall()
    #print("myresult: ", myresult)

    if len(myresult) == 1:
        data = myresult[0][0]
        return make_response(
                jsonify(
                    {
                    "status" : 200,
                    "Mensaje":"datos obtenidos",
                    "stock":data
                    }
                ),
                200
        )
    else:
        return make_response(
                jsonify(
                    {
                    "status" : 500,
                    "Mensaje":"Error interno en el servidor"
                    }
                ),
                500
        )
    
# get all producto
@inventario.route("/getproductos",methods=['GET'])
def getproductos():

    mycursor = mydb.cursor()
    query = "SELECT nombre, precio, costo, stock, categoria, sku\
        FROM producto, categoria WHERE categoria.idcategoria = producto.idcategoria"

    mycursor.execute(query, ())

    #myresult = mycursor.fetchall()
    #print("myresult: ", myresult)

    data = []
    for row in mycursor.fetchall():
        row_act = {
            "nombre":row[0],
            "precio":row[1],
            "costo":row[2],
            "stock":row[3],
            "categoria":row[4],
            "sku":row[5]
        }
        data.append(row_act)

    #print("data: ", data)
    return make_response(
                jsonify(
                    {
                    "status" : 200,
                    "Mensaje":"datos obtenidos",
                    "productos":data
                    }
                ),
                200
        )
    
# get all producto externo
@inventario.route("/getproductos_externo",methods=['GET'])
def getproductos_externo():

    mycursor = mydb.cursor()
    query = "SELECT sku, nombre, precio\
        FROM producto_simul"

    mycursor.execute(query, ())


    data = []
    for row in mycursor.fetchall():
        row_act = {
            "sku":row[0],
            "nombre":row[1],
            "precio":row[2]
        }
        data.append(row_act)

    #print("data: ", data)
    return make_response(
                jsonify(
                    {
                    "status" : 200,
                    "msg":"datos obtenidos",
                    "productos":data
                    }
                ),
                200
        )
    

# get info producto
@inventario.route("/getinfo/<sku>",methods=['GET'])
def getinfo(sku):

    mycursor = mydb.cursor()
    query = "SELECT nombre, precio, costo, stock, idcategoria FROM producto\
    WHERE sku = %s"

    mycursor.execute(query, (sku,))
    myresult = mycursor.fetchone()

    if not myresult is None:
        print("myresult: ", myresult)
        producto = {
            "nombre":myresult[0],
            "precio":myresult[1],
            "costo":myresult[2],
            "stock":myresult[3],
            "idcategoria":myresult[4]
        }
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje":"datos obtenidos",
                        "producto":producto
                        }
                    ),
                    200
            )
    else:
        return make_response(
                jsonify(
                    {
                    "status" : 500,
                    "Mensaje":"no datos encontrados"
                    }
                ),
                500
        )
    
# actualizar stock producto
@inventario.route("/actualizarstock",methods=['PUT'])
def actualizarstock():

    mycursor = mydb.cursor()
    query_suma = "UPDATE producto SET stock = stock + %s\
    WHERE sku = %s"
    query_resta = "UPDATE producto SET stock = stock - %s\
    WHERE sku = %s"

    try:
        sku = request.json['sku']
        stock = request.json['stock']
        tipo = request.json['tipo']

        if tipo == "S":
            res = mycursor.execute(query_suma, (stock, sku))
        elif tipo == "R":
            res = mycursor.execute(query_resta, (stock, sku))

        mydb.commit()

        mycursor.close()
        #mydb.close()
        #print("res", res)
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje":"Se actualizó stock correctamente",
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
    

# actualizar datos producto
@inventario.route("/modproducto",methods=['PUT'])
def modproducto():

    mycursor = mydb.cursor()
    query = "UPDATE producto SET nombre = %s, precio = %s, costo = %s,\
    stock = %s, idcategoria = %s\
    WHERE sku = %s"

    try:
        nombre = request.json['nombre']
        precio = request.json['precio']
        costo = request.json['costo']
        stock = request.json['stock']
        idcategoria = request.json['idcategoria']
        idproducto = request.json['idproducto']


        res = mycursor.execute(query, (nombre, precio, costo, stock, idcategoria, idproducto))

        mydb.commit()

        mycursor.close()
        #mydb.close()
        #print("res", res)
        return make_response(
                    jsonify(
                        {
                        "status" : 200,
                        "Mensaje":"se actualizó registro correctamente",
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