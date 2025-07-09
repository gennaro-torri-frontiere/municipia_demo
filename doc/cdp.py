CDP_API_DOC = {
    "summary": "Post CDP data",
    "description": """Estrae le entita dall'atto di liquidazione.
le entità sono:
- cup: il codice unico di progetto, un codice alfanumerico che identifica un progetto
- importo_totale: l'importo totale del certificato di pagamento in euro
- impresa: il nome dell'impresa beneficiaria del pagamento
""",
    "responses": {
        200: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "example": {
                        "cup":"string",
                        "importo_totale": 0,
                        "impresa": "string"
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