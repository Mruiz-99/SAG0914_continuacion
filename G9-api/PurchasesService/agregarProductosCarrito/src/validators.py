from wtforms import Form, IntegerField
from wtforms.validators import DataRequired, NumberRange

class AgregarProductoCarrito(Form):
    id_producto = IntegerField('id_producto', [DataRequired('Este campo es requerido'), NumberRange(min=1, message='El ID del producto debe ser un entero positivo')])
    cantidad = IntegerField('cantidad', [ NumberRange(min=1, message='El numero de productos debe ser un entero positivo')])
