from langchain_core.prompts import PromptTemplate

resume_template = """You are an expert Resume Parser.
Extract ONLY the information defined in the Resume schema from the resume text below.
If any information is missing, return null (or an empty list where appropriate).
Do not invent information that is not present in the resume.

Resume:
{resume_text}
"""

resume_prompt = PromptTemplate(
    template=resume_template,
    input_variables=["resume_text"],
)



jd_match_template = """You are an expert technical recruiter.
Compare the candidate's parsed resume data against the job description below,
and produce a structured match assessment following the JDMatchResult schema.

Be objective and specific. Base matched_skills / missing_skills strictly on what's
mentioned in the JD, and check them against the resume data.

Job Description:
{jd_text}

Candidate Resume Data (JSON):
{resume_json}
"""

jd_match_prompt = PromptTemplate(
    template=jd_match_template,
    input_variables=["jd_text", "resume_json"],
)