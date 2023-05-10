import os
from langchain import OpenAI, PromptTemplate
from getpass import getpass
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv


class Summarizer:
    @staticmethod
    def page_summary(page):
        llm = OpenAI(temperature=0)
        prompt_template = "Write a single line summary of the following: {text}:"
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
        return chain.run([page])

    @staticmethod
    def get_page(pdf_loader, page_number):
        page = Document(page_content=pdf_loader.pages[page_number].extract_text(), page_number=page_number)
        return page

    @staticmethod
    def summary(pdf_loader, page_number):
        load_dotenv()
        page = Summarizer.get_page(pdf_loader, page_number)
        page_summary = Summarizer.page_summary(page)
        return page_summary
