# 🤖 Smart Resume Analyzer & Job Description Matcher

A modern AI-powered recruitment assistant that helps recruiters and job seekers evaluate resumes against job descriptions. The application extracts structured information from PDF resumes, analyzes candidate qualifications, and provides an intelligent compatibility score using Large Language Models.

---

## ✨ Key Features

* **Resume PDF Processing**

  * Reads and extracts text from multi-page PDF resumes automatically.

* **AI-Based Information Extraction**

  * Identifies candidate details, education, work experience, technical skills, certifications, and projects using structured AI outputs.

* **Job Description Matching**

  * Compares the extracted resume information with any job description and generates an overall compatibility score.

* **Skill Gap Detection**

  * Highlights matching skills, missing technologies, strengths, and improvement areas to help candidates prepare better.

* **Interactive Dashboard**

  * Built with Streamlit for an easy-to-use interface that supports resume uploads and instant analysis.

---

# 🏗️ Project Architecture

The application follows a modular architecture where every component has a dedicated responsibility.

```
Resume PDF
      │
      ▼
PDF Text Extraction
      │
      ▼
AI Resume Parsing
      │
      ▼
Structured Candidate Profile
      │
      ▼
JD Matching Engine
      │
      ▼
Analysis Report & Match Score
```

---

## 📁 Project Structure

| File         | Description                                                     |
| ------------ | --------------------------------------------------------------- |
| `app.py`     | Streamlit application and user interface                        |
| `parser.py`  | Extracts text from resumes and converts it into structured data |
| `matcher.py` | Performs resume-to-job-description comparison                   |
| `models.py`  | Contains Pydantic models for validation                         |
| `prompts.py` | Stores prompts used for AI interactions                         |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/praveshsaini8563/project1.git
```

Move into the project folder:

```bash
cd project1
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

# 🧠 How It Works

1. Upload a resume in PDF format.
2. The application extracts the resume text.
3. The LLM converts the content into structured candidate data.
4. A job description is analyzed alongside the resume.
5. The system calculates a match score and generates detailed insights.

---

# 📜 License

This project is available under the MIT License.

---

## 👨‍💻 Author

**Pravesh Saini**

If you found this project useful, consider giving it a ⭐ on GitHub.
