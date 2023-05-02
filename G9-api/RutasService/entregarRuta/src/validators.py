from wtforms import Form, StringField, EmailField, validators, DateTimeField
from wtforms.validators import Regexp, InputRequired, DataRequired

class verificarRuta(Form):
    #cui = StringField('CUI', validators=[
    #    InputRequired("Este campo es requerido"),
    #    Regexp(r'^\d{13}$', message='El CUI debe tener 13 dígitos')
    #])
    ruta = EmailField('ruta', [DataRequired('Este campo es requerido.')])
    nombres = StringField('nombres', [DataRequired('Este campo es requerido.')])
    apellidos = StringField('apellidos', [DataRequired('Este campo es requerido.')])


