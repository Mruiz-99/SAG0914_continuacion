import io
import os
import werkzeug.exceptions
from flask import Flask, request
from flask_cors import CORS

env = os.getenv('FLASK_DEBUG', '1')
if env == '1':
    from dotenv import load_dotenv

    load_dotenv(verbose=True)

from . import models, Validators


app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000
BASE = '/notification'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def send(request, form):
    attachments = []
    if 'adjuntos' in request.files:
        files = request.files.getlist('adjuntos')
        for file in files:
            if not allowed_file(file.filename):
                return {'estatus': 400, 'error': f'Formato invalido. Formatos aceptados: {ALLOWED_EXTENSIONS}',
                        'mensaje': f'Archivo {file.filename} no aceptado'}, 400
            temp = io.BytesIO(file.stream.read())
            temp.name = file.filename
            attachments.append(temp)

    return models.Email(
        to=form.para.data,
        subject=form.asunto.data,
        attachments=attachments,
        message=form.mensaje.data,
        template=form.plantilla.data,
        title=form.titulo.data,
        html=form.html.data,
        data=form.data_dict).send_notification()


def create_app():
    return app


@app.route(f'{BASE}/ping')
def ping():
    return {'estatus': 200, 'mensaje': 'pong'}


@app.route(f'{BASE}/sendEmail', methods=['POST'])
def send_email():
    try:
        form = Validators.EmailForm(request.form)
        if not form.validate():
            return {'estatus': 400, 'error': form.errors, 'mensaje': 'Error con los campos.'}, 400
        status = send(request, form)
        return ({'estatus': 200, 'mensaje': 'Correo enviado'}, 200) \
            if not status else ({'estatus': 500, 'error': status, 'mensaje': 'Error al enviar correo'}, 500)
    except werkzeug.exceptions.RequestEntityTooLarge as err:
        return {'estatus': 413, 'error': err.__str__(), 'mensaje': 'Error al enviar correo'}, 413
