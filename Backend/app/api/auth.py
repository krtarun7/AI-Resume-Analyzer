from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database.crud import (
    create_user,
    get_user_by_email,
    save_otp,
    get_user_otp,
    verify_user,
    delete_otp,
    update_password,
)

from app.services.auth_service import (
    generate_otp,
    otp_expiry,
)

from app.services.email_service import send_otp_email

from app.security import (
    hash_password,
    verify_password,
    create_access_token,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


# ====================================
# Request Models
# ====================================

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str


class OTPRequest(BaseModel):
    email: str
    otp: str = ""


class LoginRequest(BaseModel):
    email: str
    password: str


class ResetPasswordRequest(BaseModel):
    email: str
    password: str


# ====================================
# Signup
# ====================================

@router.post("/signup")
async def signup(request: SignupRequest):

    existing_user = get_user_by_email(request.email)

    if existing_user:

        if existing_user.is_verified:
            raise HTTPException(
                status_code=400,
                detail="Email already registered."
            )

        otp = generate_otp()
        expiry = otp_expiry()

        save_otp(
            request.email,
            otp,
            expiry
        )

        await send_otp_email(
            request.email,
            otp
        )

        return {
            "message": "Account already exists but is not verified. New OTP has been sent."
        }

    hashed_password = hash_password(request.password)

    create_user(
        request.name,
        request.email,
        hashed_password
    )

    otp = generate_otp()

    expiry = otp_expiry()

    save_otp(
        request.email,
        otp,
        expiry
    )

    await send_otp_email(
        request.email,
        otp
    )

    return {
        "message": "OTP sent successfully."
    }


# ====================================
# Verify Signup OTP
# ====================================

@router.post("/verify-otp")
def verify_signup_otp(request: OTPRequest):

    otp_record = get_user_otp(request.email)

    if otp_record is None:
        raise HTTPException(
            status_code=404,
            detail="OTP not found."
        )

    if otp_record.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="OTP expired."
        )

    if otp_record.otp != request.otp:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP."
        )

    verify_user(request.email)

    delete_otp(request.email)

    return {
        "message": "Account verified successfully."
    }


# ====================================
# Resend OTP
# ====================================

@router.post("/resend-otp")
async def resend_otp(request: OTPRequest):

    user = get_user_by_email(request.email)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    if user.is_verified:
        raise HTTPException(
            status_code=400,
            detail="Account already verified."
        )

    otp = generate_otp()

    expiry = otp_expiry()

    save_otp(
        request.email,
        otp,
        expiry
    )

    await send_otp_email(
        request.email,
        otp
    )

    return {
        "message": "New OTP sent successfully."
    }


# ====================================
# Login
# ====================================

@router.post("/login")
def login(request: LoginRequest):

    user = get_user_by_email(request.email)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=401,
            detail="Please verify your email first."
        )

    if not verify_password(
        request.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password."
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "message": "Login successful.",
        "access_token": token,
        "token_type": "bearer",
        "name": user.name,
        "email": user.email
    }


# ====================================
# Forgot Password
# ====================================

@router.post("/forgot-password")
async def forgot_password(request: OTPRequest):

    user = get_user_by_email(request.email)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    otp = generate_otp()

    expiry = otp_expiry()

    save_otp(
        request.email,
        otp,
        expiry
    )

    await send_otp_email(
        request.email,
        otp
    )

    return {
        "message": "OTP sent successfully."
    }


# ====================================
# Verify Reset OTP
# ====================================

@router.post("/verify-reset-otp")
def verify_reset_otp(request: OTPRequest):

    otp_record = get_user_otp(request.email)

    if otp_record is None:
        raise HTTPException(
            status_code=404,
            detail="OTP not found."
        )

    if otp_record.expires_at < datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="OTP expired."
        )

    if otp_record.otp != request.otp:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP."
        )

    return {
        "message": "OTP verified successfully."
    }


# ====================================
# Reset Password
# ====================================

@router.post("/reset-password")
def reset_password(request: ResetPasswordRequest):

    user = get_user_by_email(request.email)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    hashed_password = hash_password(
        request.password
    )

    update_password(
        request.email,
        hashed_password
    )

    delete_otp(
        request.email
    )

    return {
        "message": "Password updated successfully."
    }