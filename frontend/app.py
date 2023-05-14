import streamlit as st
import requests
import io, os, sys
from PIL import Image


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

if st.button('Summarize page by page'):
    status = True
    page_number = 0
    while status:
        response = requests.get("http://localhost:8000/summary", params={"page_number": page_number})
        if response.status_code == 200:
            st.write("Page number: ", page_number)
            st.write(response.json()["summary"])
            page_number += 1
        elif response.status_code == 404:
            status = False
            st.write("End of document")
        else:
            status = False
            st.write(f"Error getting page summary for page number :{ page_number }")
