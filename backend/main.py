import uvicorn
import io
from fastapi import FastAPI, File, UploadFile
from processing import Summarizer
import PyPDF2


app = FastAPI()


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    file_buffer = io.BytesIO(file.file.read())
    pdf_reader = PyPDF2.PdfReader(file_buffer)
    app.state.PDFREADER = pdf_reader
    return {"text": pdf_reader.pages[1].extract_text()}

@app.get("/summary")
def get_summary(page_number: int):
    pdfreader = app.state.PDFREADER
    status = page_number < len(pdfreader.pages)
    if status:
        page_summary = Summarizer.summary(pdfreader, page_number)
    return {"summary":page_summary, "status": status}
