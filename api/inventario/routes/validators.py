from wtforms import Form, StringField , validators, MultipleFileField, DecimalField, IntegerField
from wtforms.validators import Regexp, InputRequired, DataRequired

class agregarProducto(Form):
    nombre = StringField('nombres', [DataRequired('Este campo es requerido.')])
    descripcion = StringField('descripcion', [DataRequired('Este campo es requerido.')])
    precio_costo = DecimalField('precio_costo', validators=[validators.DataRequired("Este campo es requerido.")])
    archivo = MultipleFileField('archivo')
    unidades_disponibles = IntegerField('sueldo',validators=[validators.DataRequired("Este campo es requerido.")])
    precio_unitario = DecimalField('precio_unitario', validators=[validators.DataRequired("Este campo es requerido.")])
    id_categoria = IntegerField('id_categoria',validators=[validators.DataRequired("Este campo es requerido.")])
    sku = IntegerField('sku',validators=[validators.DataRequired("Este campo es requerido.")])
