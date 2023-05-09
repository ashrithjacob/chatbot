import os
from langchain import OpenAI, PromptTemplate
from getpass import getpass
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader

DOC = "../docs/paper_1.pdf"
# Load the OpenAI API key from the environment
OPENAI_API_KEY = getpass()
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def get_pages(DOC):
    loader = PyPDFLoader(DOC)
    pages = loader.load_and_split()
    pages_list = [Document(page_content=pages[i].page_content, page_number=i) for i in range(len(pages))]
    return pages_list

def single_page_summary(page, page_number):
    llm = OpenAI(temperature=0) 
    prompt_template = "Write a single line summary of the following: {text} starting with- ON THIS PAGE:"
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text"])
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=PROMPT)
    return {"content":chain.run([page]), "number":page_number}

def wrapper():
    summary = ""
    pages = get_pages(DOC)
    for page_number, page in enumerate(pages):
        page_summary = single_page_summary(page, page_number)
        summary += "Page #:"+str(page_summary["number"])+"\n"+page_summary["content"]+"\n"
    return summary

"""
def test_prompt(page, page_number):
    llm = OpenAI(temperature=0) 
    prompt_template = "Write a single line summary of the following: {text}, START WITH- On {page_number}, we see:"
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["text","page_number"])
    PROMPT = PROMPT.format(text=page,page_number=page_number)
    print(PROMPT)
"""

if __name__ == "__main__":
    summary = wrapper()
    print(summary)
