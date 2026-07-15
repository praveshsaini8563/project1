import json
from parser import get_llm
from langchain_groq import ChatGroq
from models import Resume, JDMatchResult
from prompts import jd_match_prompt

def match_resume(resume_text: Resume | str | dict, job_description: str, llm: ChatGroq | None = None) -> JDMatchResult:
    llm = llm or get_llm()
    # method="function_call" ko hata kar simple structured output kiya hai
    structured_output = llm.with_structured_output(JDMatchResult)
    chain = jd_match_prompt | structured_output
    
    if hasattr(resume_text, "model_dump_json"):
        resume_json_str = resume_text.model_dump_json(indent=2)
    elif isinstance(resume_text, dict):
        resume_json_str = json.dumps(resume_text, indent=2)
    else:
        resume_json_str = str(resume_text)
        
    result: JDMatchResult = chain.invoke({
        "jd_text": job_description,
        "resume_json": resume_json_str
    })
    return result