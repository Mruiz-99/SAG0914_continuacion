from wtforms import Form, StringField
from wtforms.validators import Regexp, InputRequired, DataRequired

class eliminarUsuario(Form):
    cui = StringField('CUI', validators=[
        InputRequired("Este campo es requerido"),
        Regexp(r'^\d{13}$', message='El CUI debe tener 13 dígitos')
    ])
    
