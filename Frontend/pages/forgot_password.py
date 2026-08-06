import streamlit as st

from utils.api import (
    forgot_password,
    verify_reset_otp,
    reset_password,
)


def show_forgot_password():

    st.title("🔑 Forgot Password")

    # ----------------------------
    # Session State
    # ----------------------------

    if "reset_email" not in st.session_state:
        st.session_state.reset_email = ""

    if "otp_verified" not in st.session_state:
        st.session_state.otp_verified = False

    if "otp_sent" not in st.session_state:
        st.session_state.otp_sent = False

    # ----------------------------
    # STEP 1 : Send OTP
    # ----------------------------

    if not st.session_state.otp_sent:

        email = st.text_input("Email")

        if st.button("Send OTP"):

            if email == "":
                st.error("Please enter email.")

            else:

                response = forgot_password(email)

                if response.status_code == 200:

                    st.success("OTP sent successfully.")

                    st.session_state.reset_email = email
                    st.session_state.otp_sent = True

                    st.rerun()

                else:
                    st.error(response.json()["detail"])

        if st.button("⬅ Back to Login"):

            st.session_state.show_forgot = False
            st.rerun()

    # ----------------------------
    # STEP 2 : Verify OTP
    # ----------------------------

    elif not st.session_state.otp_verified:

        st.subheader("Verify OTP")

        otp = st.text_input("Enter OTP")

        if st.button("Verify OTP"):

            response = verify_reset_otp(
                st.session_state.reset_email,
                otp
            )

            if response.status_code == 200:

                st.success("OTP Verified.")

                st.session_state.otp_verified = True

                st.rerun()

            else:
                st.error(response.json()["detail"])

    # ----------------------------
    # STEP 3 : Reset Password
    # ----------------------------

    else:

        st.subheader("Reset Password")

        password = st.text_input(
            "New Password",
            type="password"
        )

        confirm = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Reset Password"):

            if password != confirm:
                st.error("Passwords do not match.")

            elif password == "":
                st.error("Password cannot be empty.")

            else:

                response = reset_password(
                    st.session_state.reset_email,
                    password
                )

                if response.status_code == 200:

                    st.success("Password changed successfully.")

                    st.session_state.otp_sent = False
                    st.session_state.otp_verified = False
                    st.session_state.reset_email = ""
                    st.session_state.show_forgot = False

                    st.rerun()

                else:
                    st.error(response.json()["detail"])