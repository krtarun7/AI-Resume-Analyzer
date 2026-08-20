# 🤖 AI Resume Analyzer — Backend

An AI-powered Resume Analyzer backend built using **FastAPI**, **PostgreSQL**, **Gemini AI**, and **SQLAlchemy**.

The backend provides REST APIs for user authentication, email OTP verification, password management, resume analysis, ATS scoring, skill matching, AI-generated suggestions, and resume analysis history.

---

## 📌 Features

### 🔐 User Authentication

- User Signup
- Login
- JWT Authentication
- Email OTP Verification
- Resend OTP
- Forgot Password
- Password Reset
- Password Hashing

### 📄 Resume Analysis

- Upload PDF Resume
- Accept Job Description
- Resume Parsing
- ATS Score Calculation
- Skill Matching
- Missing Skill Detection

### 🤖 AI Features

- Gemini AI Resume Suggestions
- Resume Improvement Recommendations
- ATS Optimization Suggestions

### 📊 Resume History

- Store Resume Analysis Results
- View Previous Analyses
- Delete Individual Analysis
- Clear Analysis History

### 📧 Email Services

- Signup OTP
- Password Reset OTP
- Email Verification

---

# 🛠 Tech Stack

### Backend

- FastAPI
- Python
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT Authentication
- Passlib / Bcrypt

### AI

- Google Gemini API

### Resume Parsing

- PyMuPDF
- pdfplumber
- python-docx

### Email

- aiosmtplib

---

# 📂 Project Structure

```text
AI_Resume_Analyzer/

├── Backend/
│
│   ├── app/
│   │
│   ├── api/
│   │   ├── auth.py
│   │   └── ...
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── crud.py
│   │   ├── models.py
│   │   └── ...
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── email_service.py
│   │   └── ...
│   │
│   ├── schemas.py
│   ├── security.py
│   └── ...
│
├── Backend/
│   ├── main.py
│   ├── run.py
│   ├── requirements.txt
│   └── .env_example
│
├── .gitignore
├── LICENSE
└── README.md