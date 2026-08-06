import os
from email.message import EmailMessage

import aiosmtplib
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


async def send_otp_email(receiver_email: str, otp: str):
    """
    Send OTP to the user's email.
    """

    message = EmailMessage()

    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver_email
    message["Subject"] = "AI Resume Analyzer - Email Verification OTP"

    message.set_content(
        f"""
Hello,

Your One-Time Password (OTP) for AI Resume Analyzer is:

{otp}

This OTP is valid for 5 minutes.

If you did not request this OTP, you can safely ignore this email.

Regards,
AI Resume Analyzer Team
"""
    )

    await aiosmtplib.send(
        message,
        hostname="smtp.gmail.com",
        port=587,
        start_tls=True,
        username=EMAIL_ADDRESS,
        password=EMAIL_PASSWORD,
    )