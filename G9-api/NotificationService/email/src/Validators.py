import json

from wtforms import Form, StringField, EmailField, MultipleFileField, SelectField, ValidationError
from wtforms.validators import DataRequired, Optional
from . import models


class EmailForm(Form):
    para = EmailField('para', [DataRequired('Este campo es requerido y debe ser un correo.')])
    asunto = StringField('asunto', [DataRequired('Este campo es requerido.')])
    adjuntos = MultipleFileField('adjuntos', [Optional()])
    mensaje = StringField()
    plantilla = SelectField(choices=list(models.templates.items()), default='notification')
    titulo = StringField(default='')
    html = StringField()
    data = StringField()

    def validate_html(form, field):
        if not form.mensaje.data and not field.data:
            raise ValidationError('html es requerido, si no se envía el parámetro mensaje')
        elif field.data and len(field.data.strip()) < 10:
            raise ValidationError('html debe de tener una longitud mayor o igual a 10 chars')

    def validate_mensaje(form, field):
        if not form.html.data and not field.data:
            raise ValidationError('mensaje es requerido, si no se envía el parámetro html')
        elif field.data and len(field.data.strip()) < 10:
            raise ValidationError('mensaje debe de tener una longitud mayor o igual a 10 chars')

    def validate_data(form, field):
        try:
            form.data_dict = json.loads(field.data) if field.data else None
        except Exception as e:
            raise ValidationError('el campo no contiene un formato de JSON válido.')
