import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000/history"


def show_profile():

    if not st.session_state.get("logged_in", False):
        st.warning("Please login first.")
        st.stop()

    st.title("👤 User Profile")

    # User Information
    st.text_input(
        "Name",
        value=st.session_state.get("user_name", ""),
        disabled=True,
    )

    st.text_input(
        "Email",
        value=st.session_state.get("user_email", ""),
        disabled=True,
    )

    st.text_input(
        "Preferred Role",
        value="Software Engineer",
        disabled=True,
    )

    st.divider()

    history = []

    try:
        response = requests.get(BACKEND_URL, timeout=5)

        if response.status_code == 200:
            history = response.json()

    except requests.RequestException:
        pass

    total = len(history)

    if total:
        avg = round(
            sum(item.get("ats_score", 0) for item in history) / total,
            2,
        )
        best = max(item.get("ats_score", 0) for item in history)
    else:
        avg = 0
        best = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Resumes Analyzed", total)

    with col2:
        st.metric("Average ATS", f"{avg}%")

    with col3:
        st.metric("Best ATS", f"{best}%")

    st.divider()

    st.success("Profile information loaded successfully.")