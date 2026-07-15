import os
import tempfile
import getpass

from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader

from models import Resume
from prompts import resume_prompt

def load_resume_text_from_bytes(file: bytes, suffix=".pdf"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file)
        tmp_path = tmp.name
    try:
        loader = PyPDFLoader(tmp_path)
        docs = loader.load()
        parser_data = "\n".join(doc.page_content for doc in docs)
        print(parser_data)
        return parser_data
    finally:
        os.remove(tmp_path)

def get_llm():
    return ChatGroq(model="llama-3.3-70b-versatile")

def parse_resume(resume_text: str, llm: ChatGroq | None = None) -> Resume:
    llm = llm or get_llm()
    # method="function_call" ko hata kar simple structured output kiya hai
    structured_llm = llm.with_structured_output(Resume)
    chain = resume_prompt | structured_llm
    result: Resume = chain.invoke({"resume_text": resume_text})
    return result