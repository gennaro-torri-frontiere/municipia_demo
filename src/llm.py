import json
import os
from openai import OpenAI
from pydantic import BaseModel

from dotenv import load_dotenv
load_dotenv()

class FatturaModel(BaseModel):
    numero: str
    importo: float
    data: str
    cig: str


class ADLModel(BaseModel):
    cup: str
    ragione_sociale_beneficiario: str
    cf_beneficiario: str
    fatture: list[FatturaModel]


class CDPModel(BaseModel):
    cup: str
    importo_totale: float


class DURCModel(BaseModel):
    scadenza_validità: str


def durc_info(text: str) -> dict:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_prompt = """
    Sei un assistente: ti viene dato un testo estratto con pytesserecat da un "DURC" e devi estrarre alcune entita da ritornare ad un algoritmo tramite JSON.
    le entità sono:
    - scadenza_validità: la data di scadenza della validità del DURC
    NB. ogni info la trovi dentro il testo quindi non inventarti nulla! se non è presente restituisci il valore '' (stringa vuota).
    """

    messages = [
        {
            "role": "system", "content": system_prompt},
        {
            "role": "user", "content": f'ecco il testo estratto: {text}'
        },
    ]

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.0,
        max_tokens=1000,
        response_format=DURCModel
    )
    
    return json.loads(completion.choices[0].message.content)

def adl_info(text: str) -> dict:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_prompt = """
    Sei un assistente: ti viene dato un testo estratto con pytesserecat da un "Atto di liquidazione" e devi estrarre alcune entita da ritornare ad un algoritmo tramite JSON.
    le entità sono:
    - cup: il codice unico di progetto, un codice alfanumerico che identifica un progetto
    - ragione_sociale_beneficiario: il nome o ragione sociale del beneficiario del pagamento
    - cf_beneficiario: il codice fiscale del beneficiario del pagamento
    - fatture: questa è una lista di entità rappresentate da un dict che contiene:
        - numero: il numero della fattura
        - importo: l'importo della fattura in euro
        - data: la data della fattura
        - cig: il codice identificativo della gara
    ogni info la trovi dentro il testo quindi non inventarti nulla! se non è presente restituisci il valore '' (stringa vuota).
    """

    messages = [
        {
            "role": "system", "content": system_prompt},
        {
            "role": "user", "content": f'ecco il testo estratto: {text}'
        },
    ]

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.0,
        max_tokens=1000,
        response_format=ADLModel
    )
    
    return json.loads(completion.choices[0].message.content)

def cdp_info(text: str) -> dict:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_prompt = """
    Sei un assistente: ti viene dato un testo estratto con pytesserecat da un "certificato di pagamento" e devi estrarre alcune entita da ritornare ad un algoritmo tramite JSON.
    le entità sono:
    - cup: il codice unico di progetto, un codice alfanumerico che identifica un progetto
    - importo_totale: l'importo totale del certificato di pagamento in euro
    """

    messages = [
        {
            "role": "system", "content": system_prompt},
        {
            "role": "user", "content": f'ecco il testo estratto: {text}'
        },
    ]

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.0,
        max_tokens=1000,
        response_format=CDPModel
    )
    
    return json.loads(completion.choices[0].message.content)
