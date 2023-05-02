from wtforms import Form, StringField, EmailField, validators, DateTimeField
from wtforms.validators import Regexp, InputRequired, DataRequired

class agendarEntrevista(Form):
    #cui = StringField('CUI', validators=[
    #    InputRequired("Este campo es requerido"),
    #    Regexp(r'^\d{13}$', message='El CUI debe tener 13 dígitos')
    #])
    correo = EmailField('correo', [DataRequired('Este campo es requerido y debe ser un correo.')])
    nombres = StringField('nombres', [DataRequired('Este campo es requerido.')])
    apellidos = StringField('apellidos', [DataRequired('Este campo es requerido.')])
    fechaCita = DateTimeField('fechaCita', validators=[validators.DataRequired()], format='%Y-%m-%d %H:%M:%S')


