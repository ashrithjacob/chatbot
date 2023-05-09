import streamlit as st
import io, os, sys
import PyPDF2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from backend.processing import Summarizer


st.title('AI POWERED PDF SUMMARY!')
st.write('Simply upload your pdf file and get a page by page summary!')

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    file_buffer = io.BytesIO(uploaded_file.read())
    pdfReader = PyPDF2.PdfReader(file_buffer)
    summary = Summarizer.create_summary(pdfReader)
    st.write(summary)
