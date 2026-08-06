import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def improve_resume(resume_text, job_description):
    """
    Generate AI-powered resume improvement suggestions using Gemini.
    """

    prompt = f"""
You are an expert ATS Resume Reviewer.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume and provide:

1. ATS Score Improvement Tips
2. Missing Technical Skills
3. Resume Summary Improvements
4. Project Improvements
5. Experience Improvements
6. Resume Formatting Suggestions
7. Final Overall Recommendation

Return the response in clear bullet points.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt,
        )

        if response.text:
            return response.text

        return "No AI suggestions were generated."

    except Exception as e:
        return f"""AI Resume Suggestions are temporarily unavailable.

Reason:
{str(e)}

Please check:
• Gemini API Key
• Internet Connection
• API Quota / Billing
• Gemini API Status
"""