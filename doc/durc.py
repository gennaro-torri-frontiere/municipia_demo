DUCR_API_DOC = {
    "summary": "Post CDP data",
    "description": """Estrae le entita dal durc
le entità sono:
- scadenza_validità: la data di scadenza della validità del DURC
- valid: un booleano che indica se il DURC è valido (scadenza_validità > data corrente)
""",
    "responses": {
        200: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "example": {
                        "scadenza_validità": "GG/MM/YYYY",
                        "valid": True
                    }
                }
            }
        },
        400: {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Invalid input data"
                    }
                }
            }
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "example": {
                        "error": "An unexpected error occurred"
                    }
                }
            }
        }
    }
}