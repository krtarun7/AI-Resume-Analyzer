import streamlit as st


def show_upload_card():

    st.subheader("📄 Upload Your Resume")
    st.caption("Supported format: PDF")

    uploaded_file = st.file_uploader(
        "Choose your resume",
        type=["pdf"],
        help="Only PDF files are supported.",
    )

    if uploaded_file is not None:
        st.success(f"✅ {uploaded_file.name}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("File Size", f"{uploaded_file.size / 1024:.2f} KB")

        with col2:
            st.metric("File Type", "PDF")

    return uploaded_file