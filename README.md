# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using **FastAPI**, **Streamlit**, **Gemini AI**, and **SQLite** that evaluates resumes against job descriptions, calculates ATS scores, identifies missing skills, and provides AI-generated resume improvement suggestions.

---

## 📌 Features

- 🔐 User Authentication
  - Sign Up
  - Login
  - Email OTP Verification
  - Forgot Password
  - Password Reset

- 📄 Resume Analysis
  - Upload PDF Resume
  - Paste Job Description
  - Resume Parsing
  - ATS Score Calculation
  - Skill Matching

- 🤖 AI Features
  - Gemini AI Resume Suggestions
  - Resume Improvement Tips
  - ATS Optimization Recommendations

- 📊 Dashboard
  - Resume Analytics
  - ATS Score Statistics
  - Recent Resume History
  - Charts & Metrics

- 📁 Resume History
  - View Previous Analyses
  - Delete Individual Records
  - Clear History

- 👤 User Profile
  - User Information
  - Resume Statistics

---

# 🛠 Tech Stack

## Frontend

- Streamlit
- Python
- Plotly
- HTML/CSS

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Pydantic

## AI

- Google Gemini API

## Resume Parsing

- PyMuPDF (fitz)

---

# 📂 Project Structure

```
AI_Resume_Analyzer/

├── Backend/
│
│   ├── app/
│   │
│   ├── api/
│   ├── database/
│   ├── services/
│   ├── schemas.py
│   ├── security.py
│   │
│   ├── main.py
│   ├── run.py
│   └── requirements.txt
│
├── Frontend/
│
│   ├── assets/
│   ├── components/
│   ├── pages/
│   ├── utils/
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
```

```bash
cd AI-Resume-Analyzer
```

---

## 2️⃣ Backend Setup

```bash
cd Backend
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Install Packages

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
SECRET_KEY=YOUR_SECRET_KEY

EMAIL=YOUR_EMAIL
EMAIL_PASSWORD=YOUR_APP_PASSWORD
```

Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## 3️⃣ Frontend Setup

```bash
cd Frontend
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Install Packages

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

Frontend runs on

```
http://localhost:8501
```

---

# 📸 Screenshots

## Login

> Add Screenshot Here

---

## Dashboard

> Add Screenshot Here

---

## Resume Analyzer

> Add Screenshot Here

---

## Analysis Result

> Add Screenshot Here

---

## History

> Add Screenshot Here

---

# 📈 Workflow

```
User Login
      │
      ▼
Upload Resume
      │
      ▼
Paste Job Description
      │
      ▼
Resume Parsing
      │
      ▼
ATS Score Calculation
      │
      ▼
Skill Matching
      │
      ▼
Gemini AI Suggestions
      │
      ▼
Store Analysis
      │
      ▼
Dashboard & History
```

---

# 📊 Future Improvements

- Resume Ranking
- Multi Resume Comparison
- Cover Letter Generator
- AI Interview Questions
- Resume Templates
- Export Analysis as PDF
- Cloud Deployment
- Admin Dashboard

---

# 👨‍💻 Author

**Tarun Kumar**

GitHub:
https://github.com/krtarun7

LinkedIn:
https://linkedin.com/in/krtarun7

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you like this project, please ⭐ star the repository on GitHub.
