from  jsonschema  import  Draft4Validator
from flask import request, jsonify
from functools import wraps
schema = {
    "type": "object",
    "properties": {
        "cui": {"type": "integer"},
        "idEmpleo": {"type": "integer"},
        "bonificacion": {"type": "array"},
        "extras": {"type": "array"},
        "retencion": {"type": "array"},
    },
    "required": ["cui", "idEmpleo", "bonificacion", "extras", "retencion"]
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