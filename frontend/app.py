import streamlit as st
import requests
import io, os, sys
import PyPDF2
from PIL import Image
from pdfminer.high_level import extract_text
from pdf2image import convert_from_bytes



st.title('AI POWERED PDF SUMMARY!')
st.write('Simply upload your pdf file and get a page by page summary!')

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    file = {'file': uploaded_file.getvalue()}
    response = requests.post("http://localhost:8000/upload", files=file)
    if response.status_code == 200:
        st.write("File uploaded successfully!")
        #st.write(response.json())
    else:
        st.write("Error getting object.")

if st.button('Summarize'):
    status = True
    page_number = 0
    while status:
        response = requests.get("http://localhost:8000/summary", params={"page_number": page_number})
        if response.status_code == 200:
            st.write("Page number: ", page_number)
            st.write(response.json()["summary"])
            status = response.json()["status"]
            page_number += 1
        else:
            status = False
            st.write("Error getting summary from page number: ", page_number)
