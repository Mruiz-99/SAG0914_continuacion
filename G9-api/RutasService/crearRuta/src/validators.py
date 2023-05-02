from wtforms import Form, StringField, EmailField, validators, FieldList, FormField, IntegerField
from wtforms.validators import  NumberRange, DataRequired
from wtforms.validators import ValidationError

def validate_integer_list(form, field):
    """
    Función de validación para asegurarse de que el campo es una lista de números enteros encerrados en corchetes y separados por coma.
    """
    try:
        value = field.data.strip()
        if value[0] != '[' or value[-1] != ']':
            raise ValueError('La lista debe estar encerrada en corchetes.')

        value = value[1:-1]  # Eliminar corchetes

        items = value.split(',')
        for item in items:
            if not item.strip().isdigit():
                raise ValueError('Los elementos de la lista deben ser números enteros.')
            if int(item) < 1 or int(item) > 24:
                raise ValueError('Los elementos de la lista debe permanecer en el rango de 1 a 24.')
    except Exception as e:
        raise ValidationError(str(e))

class IntegerListField(StringField):
    """
    Campo personalizado para validar una lista de números enteros.
    """
    def __init__(self, label='', validators=None, **kwargs):
        if validators is None:
            validators = [validate_integer_list]
        else:
            validators.append(validate_integer_list)

        super(IntegerListField, self).__init__(label, validators, **kwargs)


class crearRuta(Form):
    nombre = StringField('nombre', [DataRequired('Este campo es requerido.')])
    zonas = IntegerListField('Lista de números enteros', validators=[DataRequired()])





