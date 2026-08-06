import streamlit as st
from utils.api import signup, verify_otp


def show_signup():

    st.title("📝 Create Account")

    # Session state
    if "signup_email" not in st.session_state:
        st.session_state.signup_email = ""

    if "show_otp" not in st.session_state:
        st.session_state.show_otp = False

    # --------------------------
    # Signup Form
    # --------------------------

    if not st.session_state.show_otp:

        name = st.text_input("Full Name")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Signup"):

            if password != confirm_password:
                st.error("Passwords do not match.")

            elif name == "" or email == "" or password == "":
                st.error("All fields are required.")

            else:

                response = signup(
                    name,
                    email,
                    password
                )

                if response.status_code == 200:

                    st.success("OTP sent to your email.")

                    st.session_state.signup_email = email
                    st.session_state.show_otp = True

                    st.rerun()

                else:
                    st.error(response.json()["detail"])

    # --------------------------
    # OTP Verification
    # --------------------------

    else:

        st.subheader("Email Verification")

        otp = st.text_input("Enter OTP")

        if st.button("Verify OTP"):

            response = verify_otp(
                st.session_state.signup_email,
                otp
            )

            if response.status_code == 200:

                st.success("Account verified successfully!")

                st.session_state.show_otp = False
                st.session_state.signup_email = ""

                st.info("Please login with your account.")

            else:
                st.error(response.json()["detail"])