import streamlit as st
from utils.api import login


def show_login():

    st.title("🔐 Login")

    # ----------------------------
    # Session State
    # ----------------------------

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "token" not in st.session_state:
        st.session_state.token = ""

    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    if "user_email" not in st.session_state:
        st.session_state.user_email = ""

    if "show_forgot" not in st.session_state:
        st.session_state.show_forgot = False

    # ----------------------------
    # Login Form
    # ----------------------------

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        if email == "" or password == "":
            st.error("Please enter email and password.")

        else:

            response = login(
                email,
                password
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.logged_in = True
                st.session_state.token = data["access_token"]
                st.session_state.user_name = data["name"]
                st.session_state.user_email = data["email"]

                st.success("Login Successful!")

                st.rerun()

            else:
                st.error(response.json()["detail"])

    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:

        if st.button(
            "🔑 Forgot Password?",
            use_container_width=True
        ):
            st.session_state.show_forgot = True
            st.rerun()

    with col2:
        st.info("New user? Create an account from the Signup tab.")