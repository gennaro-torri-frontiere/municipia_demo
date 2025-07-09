import os
import uvicorn
from io import BytesIO
from datetime import datetime
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

from src.llm import adl_info, cdp_info, durc_info
from src.ocr import extract_text_from_pdf   
from src.utils import parse_date
from doc import ADL_API_DOC, CDP_API_DOC, DUCR_API_DOC

app = FastAPI()


@app.post("/adl", **ADL_API_DOC)
async def info(adl: UploadFile = File(...)):

    adl_byte = await adl.read()
    adl_str = extract_text_from_pdf(BytesIO(adl_byte))
    adl_dict = adl_info(adl_str)

    return JSONResponse(content=adl_dict)

@app.post("/cdp", **CDP_API_DOC)
async def info(cdp: UploadFile = File(...)):

    cdp_byte = await cdp.read()
    cdp_str = extract_text_from_pdf(BytesIO(cdp_byte))
    cdp_dict = cdp_info(cdp_str)

    return JSONResponse(content=cdp_dict)

@app.post("/durc", **DUCR_API_DOC)
async def durc(durc: UploadFile = File(...)):

    durc_byte = await durc.read()
    durc_str = extract_text_from_pdf(BytesIO(durc_byte))
    durc_dict = durc_info(durc_str)

    durc_dict["valid"] = parse_date(durc_dict["scadenza_validità"]) > datetime.now()
    
    return JSONResponse(content=durc_dict)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("APP_PORT"))
    # logger.info(f"Starting Service Image retriever {host}:{port}")
    uvicorn.run(app, host=host, port=port)
