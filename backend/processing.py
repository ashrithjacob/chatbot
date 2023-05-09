import os
from langchain import OpenAI, PromptTemplate
from getpass import getpass
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv


class Summarizer:
    @staticmethod
    def single_page_summary(page, page_number):
        llm = OpenAI(temperature=0)
        prompt_template = "Write a single line summary of the following: {text} starting with- ON THIS PAGE:"
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
        return {"content": chain.run([page]), "number": page_number}

    @staticmethod
    def make_pages(pdf_loader):
        pages = [
            Document(page_content=pdf_loader.pages[i].extract_text(), page_number=i)
            for i in range(len(pdf_loader.pages))
        ]
        return pages

    @staticmethod
    def create_summary(pdf_loader):
        load_dotenv()
        summary = ""
        pages = Summarizer.make_pages(pdf_loader)
        for page_number, page in enumerate(pages):
            page_summary = Summarizer.single_page_summary(page, page_number)
            summary += (
                "Page #:"
                + str(page_summary["number"])
                + "\n"
                + page_summary["content"]
                + "\n"
            )
        return summary
