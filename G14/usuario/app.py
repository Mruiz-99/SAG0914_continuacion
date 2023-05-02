from flask import Flask, make_response, jsonify
from flask.globals import request
from flask_cors import CORS
from routes.usuario import usuario

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

app.register_blueprint(usuario)


@app.route('/')
def index():
    return 'servier run Flask!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
