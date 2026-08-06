import streamlit as st


def footer():

    st.divider()

    st.markdown(
        """
        <div style="text-align:center;color:gray;">
            © 2026 AI Resume Analyzer <br>
            Developed using Streamlit + FastAPI
        </div>
        """,
        unsafe_allow_html=True,
    )