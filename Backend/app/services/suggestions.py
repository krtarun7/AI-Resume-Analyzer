def generate_suggestions(ats_score, matched_skills, missing_skills):
    """
    Generate resume improvement suggestions based on ATS score and skill comparison.
    """

    suggestions = []

    # ATS score suggestions
    if ats_score >= 90:
        suggestions.append("Excellent resume! Your resume matches the job description very well.")

    elif ats_score >= 75:
        suggestions.append("Good resume. A few improvements can increase your ATS score.")

    elif ats_score >= 60:
        suggestions.append("Your resume is average for this job. Add the missing skills to improve your chances.")

    else:
        suggestions.append("Your resume requires significant improvements for this role.")

    # Missing skill suggestions
    for skill in missing_skills:
        suggestions.append(f"Add experience with '{skill}' if you have worked on it.")

    # Resume writing suggestions
    suggestions.extend([
        "Include measurable achievements (e.g., 'Improved API performance by 35%').",
        "Use strong action verbs like Developed, Designed, Implemented, Optimized.",
        "Customize your professional summary according to the job description.",
        "Highlight projects that match the required technologies.",
        "Keep your resume to one page if you have less than 5 years of experience."
    ])

    # Remove duplicates
    return list(dict.fromkeys(suggestions))