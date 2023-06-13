import uvicorn
import io
from fastapi import FastAPI, File, UploadFile, HTTPException
from processing import Summarizer
import pypdf
import os


app = FastAPI()


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    file_buffer = io.BytesIO(file.file.read())
    pdf_reader = pypdf.PdfReader(file_buffer)
    app.state.PDFREADER = pdf_reader
    return {"text": pdf_reader.pages[0].extract_text()}

@app.get("/summary")
def get_summary(page_number: int):
    pdfreader = app.state.PDFREADER
    if page_number < len(pdfreader.pages):
        page_summary= Summarizer.summary(pdfreader, page_number)
        page_summary = "none"
    else:
        page_summary = "none"
        raise HTTPException(status_code=404, detail="Page not found")
    return {"summary":page_summary}

@app.get("/rawtext")
def get_rawtext(page_number: int):
    pdf_reader = app.state.PDFREADER
    if page_number >= len(pdf_reader.pages):
        raise HTTPException(status_code=404, detail="Page not found")
    return {"rawtext": pdf_reader.pages[page_number]}
