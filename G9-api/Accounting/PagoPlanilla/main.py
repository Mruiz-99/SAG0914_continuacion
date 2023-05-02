from src.app import app, env



if __name__ == '__main__':
    if env == 'development':
        from waitress import serve
        serve(app,port=3131)
    else:
        from waitress import serve
        serve(app,port=3131)


# servicio Recargar Billetera



"""
entorno virtual:

python3 -m venv env
source env/bin/activate
deactivate

export FLASK_APP=main.py
export FLASK_RUN_PORT=3131

GENERAR REQUERIMIENTOS
pipreqs --force
pip freeze > requirements.txt

GENERAR IMAGEN DOCKER
docker build -t g9-api-wallet-crear-billetera .
"""

