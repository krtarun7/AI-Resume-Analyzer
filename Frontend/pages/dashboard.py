import requests
import streamlit as st

from components.metric_cards import show_metric_cards
from components.charts import (
    show_ats_chart,
    show_score_distribution,
)

BACKEND_URL = "http://127.0.0.1:8000/history"


def show_dashboard():

    # ==========================================
    # Welcome
    # ==========================================

    st.markdown(
        f"""
        <h1 style='color:white;'>
            Welcome Back,
            <span style='color:#22C55E'>
                {st.session_state.user_name}
            </span>
            👋
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.caption("AI Powered Resume Screening Platform")

    st.write("")

    # ==========================================
    # Fetch Resume History
    # ==========================================

    try:

        response = requests.get(BACKEND_URL)

        if response.status_code == 200:
            history = response.json()
        else:
            history = []

    except Exception:
        history = []

    # ==========================================
    # Statistics
    # ==========================================

    total = len(history)

    if total > 0:

        avg = round(
            sum(item["ats_score"] for item in history) / total,
            1
        )

        best = max(
            item["ats_score"] for item in history
        )

    else:

        avg = 0
        best = 0

    # ==========================================
    # AI Rating
    # ==========================================

    if avg >= 90:
        rating = "A+"

    elif avg >= 80:
        rating = "A"

    elif avg >= 70:
        rating = "B"

    elif avg >= 60:
        rating = "C"

    else:
        rating = "D"

    # ==========================================
    # Metric Cards
    # ==========================================

    show_metric_cards(
        total,
        avg,
        best,
        rating
    )

    st.write("")
    st.divider()

    # ==========================================
    # Charts
    # ==========================================

    st.subheader("📊 Resume Analytics")

    col1, col2 = st.columns(2)

    with col1:
        show_ats_chart(history)

    with col2:
        show_score_distribution(history)

    st.divider()

    # ==========================================
    # Recent Resume Analysis
    # ==========================================

    st.subheader("📄 Recent Resume Analysis")

    if len(history) == 0:

        st.info("No resumes analyzed yet.")

        return

    latest = history[:5]

    for item in latest:

        col1, col2, col3 = st.columns([6, 2, 2])

        with col1:
            st.write(f"📄 **{item['filename']}**")

        with col2:
            st.success(f"{item['ats_score']}%")

        with col3:
            st.write("✅ Completed")

    st.divider()

    st.success("🚀 Your AI Resume Dashboard is Ready!")