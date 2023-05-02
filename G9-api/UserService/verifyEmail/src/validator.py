body_model = {
    'type': 'object',
    'properties': {
        'correo': {
            'format': 'email'
        },
        'codigoVerificacion': {
            'type': 'string'
        }
    },
    'required': ['correo', 'codigoVerificacion'],
    'additionalProperties': False
}
