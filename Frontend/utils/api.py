import requests

BASE_URL = "https://ai-resume-analyzers.onrender.com"

TIMEOUT = 30


# ==========================================
# Authentication APIs
# ==========================================

def signup(name, email, password):
    return requests.post(
        f"{BASE_URL}/auth/signup",
        json={
            "name": name,
            "email": email,
            "password": password
        },
        timeout=TIMEOUT
    )


def verify_otp(email, otp):
    return requests.post(
        f"{BASE_URL}/auth/verify-otp",
        json={
            "email": email,
            "otp": otp
        },
        timeout=TIMEOUT
    )


def login(email, password):
    return requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": email,
            "password": password
        },
        timeout=TIMEOUT
    )


# ==========================================
# Forgot Password APIs
# ==========================================

def forgot_password(email):
    return requests.post(
        f"{BASE_URL}/auth/forgot-password",
        json={
            "email": email
        },
        timeout=TIMEOUT
    )


def verify_reset_otp(email, otp):
    return requests.post(
        f"{BASE_URL}/auth/verify-reset-otp",
        json={
            "email": email,
            "otp": otp
        },
        timeout=TIMEOUT
    )


def reset_password(email, password):
    return requests.post(
        f"{BASE_URL}/auth/reset-password",
        json={
            "email": email,
            "password": password
        },
        timeout=TIMEOUT
    )


# ==========================================
# Resume APIs
# ==========================================

def analyze_resume(uploaded_file, job_description):

    files = {
        "resume": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    data = {
        "job_description": job_description
    }

    return requests.post(
        f"{BASE_URL}/analyze",
        files=files,
        data=data,
        timeout=TIMEOUT
    )


def get_history():
    return requests.get(
        f"{BASE_URL}/history",
        timeout=TIMEOUT
    )


def delete_history():
    return requests.delete(
        f"{BASE_URL}/history",
        timeout=TIMEOUT
    )


def delete_analysis(analysis_id):
    return requests.delete(
        f"{BASE_URL}/history/{analysis_id}",
        timeout=TIMEOUT
    )