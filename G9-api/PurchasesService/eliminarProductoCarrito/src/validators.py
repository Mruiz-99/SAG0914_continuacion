from wtforms import Form, IntegerField
from wtforms.validators import DataRequired, NumberRange

class EliminarProductoCarrito(Form):
    idProducto = IntegerField('idProducto', [DataRequired('Este campo es requerido'), NumberRange(min=1, message='El ID del producto debe ser un entero positivo')])
