from src.app import app, env



if __name__ == '__main__':
    if env == 'development':
        from waitress import serve
        serve(app,port=3103)
    else:
        from waitress import serve
        serve(app,port=3103)


# servicio Recargar Billetera



"""

entorno virtual:

python3 -m venv env
source env/bin/activate
deactivate

export FLASK_APP=main.py
export FLASK_RUN_PORT=3103

GENERAR REQUERIMIENTOS
pipreqs --force
pip freeze > requirements.txt

GENERAR IMAGEN DOCKER
"""


