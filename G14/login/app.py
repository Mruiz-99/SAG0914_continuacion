# importaciones
from flask import Flask, make_response, jsonify
from flask.globals import request
from flask_cors import CORS
from routes.login import login

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

app.register_blueprint(login)


@app.route('/')
def index():
    return 'servier run Flask!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
