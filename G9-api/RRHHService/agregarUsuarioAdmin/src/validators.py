from wtforms import Form, StringField, EmailField , validators, PasswordField, DecimalField
from wtforms.validators import Regexp, InputRequired, DataRequired

class agregarUsuarios(Form):
    cui = StringField('CUI', validators=[
        InputRequired("Este campo es requerido"),
        Regexp(r'^\d{13}$', message='El CUI debe tener 13 dígitos')
    ])
    correo = EmailField('correo', [DataRequired('Este campo es requerido y debe ser un correo.')])
    nombres = StringField('nombres', [DataRequired('Este campo es requerido.')])
    apellidos = StringField('apellidos', [DataRequired('Este campo es requerido.')])
    password = PasswordField('Contraseña', validators=[validators.DataRequired("Este campo es requerido.")])
    confirmarPassword = PasswordField('confirmacionContraseña', validators=[validators.DataRequired("Este campo es requerido.")])
    areaAsignada = StringField('areaAsignada', [DataRequired('Este campo es requerido.')])
    fechaNacimiento = StringField('fechaNacimiento', validators=[validators.DataRequired(), validators.Regexp('^\d{4}/\d{2}/\d{2}$', message='El formato de la fecha debe ser AAAA/MM/DD')])
    sueldo = DecimalField('sueldo',validators=[validators.DataRequired("Este campo es requerido.")])
