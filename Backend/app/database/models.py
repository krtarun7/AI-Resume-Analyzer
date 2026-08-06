from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
)

from app.database.database import Base


# ======================================
# Resume Analysis Table
# ======================================
class ResumeAnalysis(Base):
    __tablename__ = "resume_analysis"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255), nullable=False)

    ats_score = Column(Float, nullable=False)

    matched_skills = Column(Text)

    missing_skills = Column(Text)

    suggestions = Column(Text)

    resume_length = Column(Integer)


# ======================================
# Users Table
# ======================================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False, index=True)

    password = Column(String(255), nullable=False)

    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)


# ======================================
# OTP Verification Table
# ======================================
class OTPVerification(Base):
    __tablename__ = "otp_verification"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(150), nullable=False, index=True)

    otp = Column(String(6), nullable=False)

    expires_at = Column(DateTime, nullable=False)

    verified = Column(Boolean, default=False)