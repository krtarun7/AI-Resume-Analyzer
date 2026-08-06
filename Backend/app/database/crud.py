import json
import os
import shutil

from app.database.database import SessionLocal
from app.database.models import (
    ResumeAnalysis,
    User,
    OTPVerification,
)

UPLOAD_FOLDER = "uploads"


# ======================================================
# Resume Analysis
# ======================================================

def save_analysis(result):
    db = SessionLocal()

    analysis = ResumeAnalysis(
        filename=result["filename"],
        ats_score=result["ats_score"],
        matched_skills=json.dumps(result["matched_skills"]),
        missing_skills=json.dumps(result["missing_skills"]),
        suggestions=json.dumps(result["suggestions"]),
        resume_length=result["resume_length"]
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    db.close()

    return analysis


def get_all_analysis():
    db = SessionLocal()

    analyses = (
        db.query(ResumeAnalysis)
        .order_by(ResumeAnalysis.id.desc())
        .all()
    )

    result = []

    for item in analyses:
        result.append({
            "id": item.id,
            "filename": item.filename,
            "ats_score": item.ats_score,
            "matched_skills": json.loads(item.matched_skills),
            "missing_skills": json.loads(item.missing_skills),
            "suggestions": json.loads(item.suggestions),
            "resume_length": item.resume_length
        })

    db.close()

    return result


def delete_analysis(analysis_id):
    db = SessionLocal()

    analysis = (
        db.query(ResumeAnalysis)
        .filter(ResumeAnalysis.id == analysis_id)
        .first()
    )

    if analysis:

        file_path = os.path.join(
            UPLOAD_FOLDER,
            analysis.filename
        )

        if os.path.exists(file_path):
            os.remove(file_path)

        db.delete(analysis)
        db.commit()

    db.close()


def delete_all_analysis():
    db = SessionLocal()

    db.query(ResumeAnalysis).delete()

    db.commit()
    db.close()

    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ======================================================
# USER
# ======================================================

def create_user(name, email, password):
    db = SessionLocal()

    user = User(
        name=name,
        email=email,
        password=password,
        is_verified=False
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    db.close()

    return user


def get_user_by_email(email):
    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    db.close()

    return user


def verify_user(email):
    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if user:
        user.is_verified = True

    otp = (
        db.query(OTPVerification)
        .filter(OTPVerification.email == email)
        .first()
    )

    if otp:
        otp.verified = True

    db.commit()
    db.close()


def update_password(email, password):
    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if user:
        user.password = password
        db.commit()

    db.close()


# ======================================================
# OTP
# ======================================================

def save_otp(email, otp, expiry):
    db = SessionLocal()

    # Delete previous OTP
    db.query(OTPVerification).filter(
        OTPVerification.email == email
    ).delete()

    otp_record = OTPVerification(
        email=email,
        otp=otp,
        expires_at=expiry,
        verified=False
    )

    db.add(otp_record)
    db.commit()

    db.close()


def get_user_otp(email):
    db = SessionLocal()

    otp = (
        db.query(OTPVerification)
        .filter(OTPVerification.email == email)
        .order_by(OTPVerification.id.desc())
        .first()
    )

    db.close()

    return otp


def delete_otp(email):
    db = SessionLocal()

    db.query(OTPVerification).filter(
        OTPVerification.email == email
    ).delete()

    db.commit()
    db.close()