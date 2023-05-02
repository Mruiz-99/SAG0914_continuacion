from wtforms import Form, StringField, MultipleFileField
from wtforms.validators import DataRequired, Optional


class UploadForm(Form):
    archivo = MultipleFileField('archivo')
    directorio = StringField([Optional()], default='')

