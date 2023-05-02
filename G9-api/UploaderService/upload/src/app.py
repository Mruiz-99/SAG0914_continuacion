import cloudinary
import io
import os
import werkzeug.exceptions
from flask import Flask, request
from flask_cors import CORS
from . import validators
from cloudinary.uploader import upload

env = os.getenv('FLASK_DEBUG', '1')
if env == '1':
    from dotenv import load_dotenv

    load_dotenv(verbose=True)

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000
BASE = '/bucket'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def config_bucket():
    cloudinary.config(
        cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
        api_key=os.getenv('CLOUDINARY_API_KEY'),
        api_secret=os.getenv('CLOUDINARY_API_SECRET'),
        secure=True
    )


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_app():
    return app


@app.route(f'{BASE}/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}


@app.route(f'{BASE}/upload', methods=['POST'])
def upload_file():
    try:
        config_bucket()
        form = validators.UploadForm(request.form)
        if not form.validate():
            return {'estatus': 400, 'error': form.errors, 'mensaje': 'Error con los campos.'}, 400

        validated_files = []
        if 'archivo' in request.files:
            files = request.files.getlist('archivo')
            for file in files:
                if not allowed_file(file.filename):
                    return {'estatus': 400, 'error': f'Formato invalido. Formatos aceptados: {ALLOWED_EXTENSIONS}',
                            'mensaje': f'Archivo {file.filename} no aceptado'}, 400
                temp = io.BytesIO(file.stream.read())
                temp.name = file.filename
                validated_files.append(temp)
        else:
            return {'estatus': 400, 'error': 'No hay archivos por subir', 'mensaje': 'Archivo es requerido'}, 400

        if len(validated_files) == 0:
            return {'estatus': 400, 'mensaje': 'Enviar archivos a subir'}, 400

        url = list(
            map(lambda item: cloudinary.uploader.upload(item, folder=f'SA_proyecto/{form.directorio.data}').get('url'),
                validated_files))

        if len(url) > 0:
            return {'estatus': 200, 'mensaje': 'Objeto Almacenado', 'data': url}, 200
        return {'estatus': 500, 'error': 'Error al subir el/los objetos',
                'mensaje': 'No se pudo almacenar los objetos'}, 500
    except werkzeug.exceptions.RequestEntityTooLarge as err:
        return {'estatus': 413, 'error': err.__str__(), 'mensaje': 'Error al almacenar el objeto'}, 413
    except Exception as err:
        return {'estatus': 500, 'error': str(err), 'mensaje': 'Error al almacenar el objeto.'}, 500
