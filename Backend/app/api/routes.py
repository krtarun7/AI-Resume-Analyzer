import os
import shutil

from fastapi import APIRouter, File, Form, UploadFile

from app.services.parser import extract_resume_text
from app.services.ats import calculate_ats_score
from app.services.skills import compare_skills
from app.services.suggestions import generate_suggestions
from app.services.gemini_service import improve_resume

from app.database.crud import (
    save_analysis,
    get_all_analysis,
    delete_analysis,
    delete_all_analysis
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }


@router.get("/history")
def history():
    return get_all_analysis()


@router.delete("/history/{analysis_id}")
def remove_analysis(analysis_id: int):
    delete_analysis(analysis_id)
    return {
        "message": "Analysis deleted successfully"
    }


@router.delete("/history")
def clear_history():
    delete_all_analysis()
    return {
        "message": "All history deleted successfully"
    }


@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form("")
):

    # Create uploads folder
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", resume.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    try:
        # Extract Resume Text
        resume_text = extract_resume_text(file_path)

        # ATS Score
        ats_score = calculate_ats_score(
            resume_text,
            job_description
        )

        # Skill Matching
        skills = compare_skills(
            resume_text,
            job_description
        )

        # Rule-based Suggestions
        suggestions = generate_suggestions(
            ats_score,
            skills["matched_skills"],
            skills["missing_skills"]
        )

        # Gemini AI Suggestions
        try:
            ai_suggestions = improve_resume(
                resume_text,
                job_description
            )
        except Exception as e:
            ai_suggestions = (
                "AI Resume Suggestions are temporarily unavailable.\n\n"
                f"Reason: {str(e)}"
            )

        result = {
            "filename": resume.filename,
            "ats_score": ats_score,
            "matched_skills": skills["matched_skills"],
            "missing_skills": skills["missing_skills"],
            "suggestions": suggestions,
            "ai_suggestions": ai_suggestions,
            "resume_length": len(resume_text),
            "resume_text": resume_text[:1000]
        }

        save_analysis(result)

        return result

    finally:
        # Always remove uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)