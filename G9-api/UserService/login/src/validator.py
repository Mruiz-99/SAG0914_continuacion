body_model = {
    "type": "object",
    "properties": {
        "correo": {
            "format": "email"
        },
        "contraseña": {
            "type": "string"
        }
    },
    "required": ["correo", "contraseña"],
    "additionalProperties": False
}
