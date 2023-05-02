from  jsonschema  import  Draft4Validator
from flask import request, jsonify
from functools import wraps

#"montowallet", "id_detalle_carrito", "id_billetera", "id_tarjeta", "montotarjeta", "tipopago","estadopago"
schema = {
    "type": "object",
    "properties": {
        "montowallet": {"type": "integer"},
        "id_usuario": {"type": "integer"},
        "id_billetera": {"type": "integer"},
        "id_tarjeta": {"type": "integer"},
        "montotarjeta": {"type": "integer"},
        "tipopago": {"type": "integer"}
    },
    "required": ["montowallet", "id_usuario", "id_billetera", "id_tarjeta", "montotarjeta", "tipopago"]
}

def validate_schema():
    validator = Draft4Validator(schema)
    def wrapper(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            input = request.get_json(force=True)
            errors = [error.message for error in validator.iter_errors(input)]
            _errors = ', '.join(map(str, errors))
            if errors:
                response = jsonify(dict(estatus=400,
                                        error="Error al interpretar la solicitud",
                                        mensaje=_errors))
                response.status_code = 400
                return response
            else:
                return fn(*args, **kwargs)
        return wrapped
    return wrapper