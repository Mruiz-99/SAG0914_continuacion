body_model = {
    "type": "objetc",
    "properties": {
        "para": {
            "format": "email"
        },
        "asunto": {
            "type": "string"
        },
        "mensaje": {
            "type": "string"
        },
        "plantilla": {
            "type": "string",
            "enum": ["confirmEmail"]
        }
    },
    "required": ["para", "asunto", "mensaje", "plantilla"],
    "additionalProperties": False
}
