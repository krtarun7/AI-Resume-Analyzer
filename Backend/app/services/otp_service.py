import random
from datetime import datetime, timedelta


def generate_otp():
    """Generate a 6-digit OTP."""
    return str(random.randint(100000, 999999))


def otp_expiry():
    """OTP expires after 5 minutes."""
    return datetime.utcnow() + timedelta(minutes=5)


def otp_is_valid(expiry_time):
    """Check whether the OTP is still valid."""
    return datetime.utcnow() <= expiry_time