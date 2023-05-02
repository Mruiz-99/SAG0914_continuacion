from  jsonschema  import  Draft4Validator
from flask import request, jsonify
from functools import wraps
schema = {
    "type": "object",
    "properties": {
        "cui": {"type": "integer"},
        "metodo": {"type": "integer", "minimum": 1, "maximum": 2},
        "mes": {"type": "integer", "minimum": 1, "maximum": 12},
        "anio": {"type": "integer"},
        "moneda": {"type": "string"},
        "descripcion": {"type": "string"}
    },
    "required": ["cui", "metodo", "mes", "anio", "moneda", "descripcion"]
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