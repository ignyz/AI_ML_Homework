from io import BytesIO

import PyPDF2

from iocsearcher.document import open_document, open_document_bn
from lib.iocs_tool import IOCTool
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
from pydantic import BaseModel
import uvicorn
from iteration_utilities import unique_everseen

app = FastAPI()

class IOCs(BaseModel):
    ioc: str
    type: str
    confidentiality_score: float

@app.post("/extract_iocs_from_text/", response_model=List[IOCs])
async def extract_iocs_from_text(text: str):
    iocs = []
    extractor = IOCTool()

    # Extract IOCs from text
    extracted_iocs = extractor.extract_iocs(text)

    for ioc in extracted_iocs:
        iocs.append(IOCs(ioc=ioc[0], type=ioc[1], confidentiality_score=ioc[2]))

    return iocs

@app.post("/extract_doc_iocs/", response_model=List[IOCs])
async def extract_doc_iocs(file: UploadFile = File(...)):
    iocs = []
    doc_content = await file.read()
    try:
        text = open_document_bn(file, doc_content)
        # Extract IOCs from text
        extractor = IOCTool()
        extracted_iocs = extractor.extract_iocs(text)

        for ioc in extracted_iocs:
            iocs.append(IOCs(ioc=ioc[0], type=ioc[1], confidentiality_score=ioc[2]))

        # remove duplicates
        iocs = list(unique_everseen(iocs))
        return iocs

    except Exception as e:
        print(e)
        return []


if __name__ == "__main__":
    # test_form()
    uvicorn.run(app, host="127.0.0.1", port=8000)

