#from flask import Flask, make_response, jsonify
#from flask.globals import request
#from flask_cors import CORS
#from routes.usuario import usuario

#app = Flask(__name__)
#CORS(app)

#app.config["DEBUG"] = True

#app.register_blueprint(usuario)

#from src.app import app, env
from routes.usuario import app, env


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
    #if env == '1':
    #    app.run(port=5050, debug=True)
    #else:
    #    from waitress import serve
    #    serve(app, port=5050)
