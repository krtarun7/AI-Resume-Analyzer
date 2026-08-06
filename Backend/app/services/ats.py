from app.services.skills import extract_skills


def calculate_ats_score(resume_text, job_description):
    """
    Calculate ATS score based on skill matching.
    """

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    if not jd_skills:
        return 0

    matched = 0

    for skill in jd_skills:
        if skill in resume_skills:
            matched += 1

    score = (matched / len(jd_skills)) * 100

    return round(score, 2)