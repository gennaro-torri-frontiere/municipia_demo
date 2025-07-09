ADL_API_DOC = {
    "summary": "Post ADL data",
    "description": """Estrae le entita dall'atto di liquidazione
le entità sono:
- cup: il codice unico di progetto, un codice alfanumerico che identifica un progetto
- ragione_sociale_beneficiario: il nome o ragione sociale del beneficiario del pagamento
- cf_beneficiario: il codice fiscale del beneficiario del pagamento
- fatture: questa è una lista di entità rappresentate da un dict che contiene:
    - numero: il numero della fattura
    - importo: l'importo della fattura in euro
    - data: la data della fattura
    - cig: il codice identificativo della gara
""",
    "responses": {
        200: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "example": {
                        "cup": "string",
                        "ragione_sociale_beneficiario": "string",
                        "cf_beneficiario": "12345678901",
                        "fatture": [
                            {
                                "numero": "string",
                                "importo": 0,
                                "data": "GG/MM/YYYY",
                                "cig": "string"
                            },
                            {
                                "numero": "string",
                                "importo": 0,
                                "data": "GG/MM/YYYY",
                                "cig": "string"
                            }
                        ]
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