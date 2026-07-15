

---

# 📄 AI Resume Analyzer & JD Matcher

An intelligent, production-ready recruitment companion that acts as a digital recruiter. It processes messy, unstructured resume PDFs, transforms them into strictly validated data structures, and objectively benchmarks them against job descriptions using **LangChain**, **Groq (Llama 3.3 70B)**, and **Streamlit**.

---

## 🚀 Features

* **Intelligent PDF Parsing:** Converts raw, multi-page PDF documents into precise, structured text data.


* **Structured Schema Extraction:** Maps raw text directly into strongly-typed Pydantic schemas, extracting candidate profiles, education details, GPAs, experience, tech stacks, and core skills.


* **Objective JD Benchmarking:** Computes a calculated match score (0–100%) against any pasted Job Description, free from human fatigue or hiring bias.


* **Deep Gap Analysis:** Generates bulleted lists of matched skills, missing skills, candidate strengths, and critical competency gaps, complete with a professional summary.


* **Interactive UI & Working Memory:** Built with an elegant Streamlit interface that leverages session states to avoid browser refresh amnesia.



---

## 🧠 Architecture & Cognitive Blueprint

This application is designed around **Cognitive Systems Architecture**, breaking down the complex recruitment workflow into modular, decoupled Python components.

```
[ Raw PDF Resume ] ──( Sensation: PyPDFLoader )──> [ Raw Text String ]
                                                           │
[ Structured JSON ] <──( Perception: Llama 3.3 70B )───────┘
        │
        ├──> ( Memory: Pydantic Schema Validation )
        │
        └──> ( Judgment: Matcher Pipeline ) ──> [ Interactive Streamlit UI ]

```

### File Roles & Operational Mapping

| File | Core Role | Technical Implementation |
| --- | --- | --- |
| **`app.py`** | **The Interface & Working Memory**<br> | Streamlit UI layer, user interaction, file handling, and `st.session_state` management.

 |
| **`parser.py`** | **The Senses & Perception Layer**<br> | Extracts byte-streams via `PyPDFLoader` and drives structured LLM output generation.

 |
| **`matcher.py`** | **The Judgment & Evaluation Layer**<br> | Compares the structured candidate profile against text-based JDs.

 |
| **`models.py`** | **The Mental Schema / Blueprint**<br> | Standardizes data schemas using Pydantic models (`Resume`, `Education`, `Experience`, `JDMatchResult`).

 |
| **`prompts.py`** | **The System Operational Rules**<br> | Sets boundaries, enforces factual contexts, and isolates LLM prompts to prevent hallucinations.

 |

---

## 🛠️ Tech Stack

* **Frontend Framework:** Streamlit


* **Orchestration Engine:** LangChain / LangChain Core


* **LLM Inference Provider:** Groq Cloud (Model: `llama-3.3-70b-versatile`)


* **Data Validation:** Pydantic v2


* **Document Parsing:** PyPDF (via LangChain Community loaders)



---

## ⚙️ Installation & Setup

Follow these steps to set up and launch the application locally.

### 1. Clone the Project & Move into Directory

```bash
git clone <repository-url>
cd resume-analyzer

```

### 2. Isolate Environment & Install Dependencies

Create a clean virtual environment to prevent package version conflicts:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install -r requirements.txt

```

### 3. Configure Your Environment Variables

The application requires a Groq API Key for processing model inferences.

```bash
cp .env.example .env

```

Open your newly created `.env` file and insert your API credential:

```env
GROQ_API_KEY=gsk_your_secure_groq_api_key_here

```

### 4. Run the Application

Start the local Streamlit development server:

```bash
streamlit run app.py

```

The application will automatically launch and become accessible at: **`http://localhost:8501`**

---

## 🔍 Under the Hood: The 4-Step Chain Pattern

Every structured AI transaction in this codebase follows a deterministic, pipeline architecture:

> **The Processing Pipeline:**
> `PromptTemplate` ➔ `LLM with Structured Output` ➔ `Pipe Operator (|)` ➔ `Invoke`
> 

```python
# A look into the decoupled, deterministic processing pipeline (parser.py)
def parse_resume(resume_text: str, llm: ChatGroq | None = None) -> Resume:
    llm = llm or get_llm()
    structured_llm = llm.with_structured_output(Resume, method="function_calling")
    chain = resume_prompt | structured_llm
    result: Resume = chain.invoke({"resume_text": resume_text})
    return result

```

* **Strict Factuality:** Driven by a deterministic temperature of `0`, the parsing machine is completely locked into your input file—preventing speculative hallucinations and ensuring repeatable, audit-ready data.



---

### Shukriya! 🙏

Thank you for exploring this architecture! Today, you have seen how mapping human cognitive models directly into software design principles creates more reliable, scalable, and modular AI applications.