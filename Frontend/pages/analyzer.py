import streamlit as st
import time

from utils.api import analyze_resume
from components.upload_cards import show_upload_card


def show_analyzer():

    st.title("🤖 AI Resume Analyzer")
    st.caption("Upload your resume and compare it with a Job Description.")

    st.write("")

    # Job Description
    job_description = st.text_area(
        "📋 Paste Job Description",
        height=220,
        placeholder="Paste the complete job description here..."
    )

    st.write("")

    # Resume Upload
    uploaded_file = show_upload_card()

    st.write("")

    if uploaded_file is not None:

        if st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        ):

            if job_description.strip() == "":
                st.warning("Please paste a Job Description.")
                return

            with st.spinner("Analyzing Resume..."):

                time.sleep(1)

                response = analyze_resume(
                    uploaded_file,
                    job_description
                )

            if response.status_code != 200:

                st.error(response.text)
                return

            result = response.json()

            st.success("Analysis Completed Successfully!")

            st.divider()

            # ATS Score
            st.subheader("🎯 ATS Score")

            st.progress(result["ats_score"] / 100)

            st.metric(
                "Overall Score",
                f"{result['ats_score']}%"
            )

            st.divider()

            # Skills
            col1, col2 = st.columns(2)

            with col1:

                st.subheader("✅ Matched Skills")

                for skill in result["matched_skills"]:
                    st.success(skill)

            with col2:

                st.subheader("❌ Missing Skills")

                for skill in result["missing_skills"]:
                    st.error(skill)

            st.divider()

            # Suggestions
            st.subheader("💡 Suggestions")

            for suggestion in result["suggestions"]:
                st.info(suggestion)

            st.divider()

            # AI Suggestions
            st.subheader("🤖 Gemini AI Suggestions")

            st.write(result["ai_suggestions"])

            st.success("Resume Analysis Completed 🚀")