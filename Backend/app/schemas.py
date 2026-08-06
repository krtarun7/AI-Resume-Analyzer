from pydantic import BaseModel


class AnalyzeResponse(BaseModel):
    ats_score: int
    matched_skills: list[str]
    missing_skills: list[str]
    suggestions: list[str]