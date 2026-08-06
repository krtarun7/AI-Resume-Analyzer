from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database.database import SessionLocal
from app.database.models import User, OTPVerification

from app.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.services.otp_service import (
    generate_otp,
    otp_expiry
)

from app.services.email_service import send_otp_email

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==========================
# Request Models
# ==========================

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str


class OTPRequest(BaseModel):
    email: str
    otp: str


class LoginRequest(BaseModel):
    email: str
    password: str


# ==========================
# Signup
# ==========================

@router.post("/signup")
async def signup(request: SignupRequest):

    db = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if existing_user:
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    hashed_password = hash_password(request.password)

    user = User(
        name=request.name,
        email=request.email,
        password=hashed_password,
        is_verified=False
    )

    db.add(user)
    db.commit()

    otp = generate_otp()

    otp_record = OTPVerification(
        email=request.email,
        otp=otp,
        expires_at=otp_expiry(),
        verified=False
    )

    db.add(otp_record)
    db.commit()
    db.close()

    await send_otp_email(request.email, otp)

    return {
        "message": "OTP sent successfully."
    }


# ==========================
# Verify OTP
# ==========================

@router.post("/verify-otp")
def verify_signup_otp(request: OTPRequest):

    db = SessionLocal()

    otp_record = (
        db.query(OTPVerification)
        .filter(
            OTPVerification.email == request.email,
            OTPVerification.verified == False
        )
        .order_by(OTPVerification.id.desc())
        .first()
    )

    if not otp_record:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="OTP not found."
        )

    if otp_record.expires_at < datetime.utcnow():
        db.close()
        raise HTTPException(
            status_code=400,
            detail="OTP expired."
        )

    if otp_record.otp != request.otp:
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP."
        )

    otp_record.verified = True

    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if user:
        user.is_verified = True

    db.commit()
    db.close()

    return {
        "message": "Email verified successfully."
    }


# ==========================
# Login
# ==========================

@router.post("/login")
def login(request: LoginRequest):

    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if not user:
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if not verify_password(
        request.password,
        user.password
    ):
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if not user.is_verified:
        db.close()
        raise HTTPException(
            status_code=401,
            detail="Please verify your email first."
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    db.close()

    return {
        "access_token": token,
        "token_type": "bearer",
        "name": user.name,
        "email": user.email
    }