import requests
import pandas as pd
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"


def show_history():

    st.title("📜 Resume Analysis History")

    # ==========================
    # Fetch History
    # ==========================
    try:
        response = requests.get(f"{BASE_URL}/history")

        if response.status_code != 200:
            st.error("Unable to fetch history.")
            return

        history = response.json()

    except Exception as e:
        st.error(f"Backend Error: {e}")
        return

    if not history:
        st.info("No resume analyses found.")
        return

    # ==========================
    # Clear All Button
    # ==========================
    col1, col2 = st.columns([3, 1])

    with col2:
        if st.button("🗑 Clear All", width="stretch"):

            requests.delete(f"{BASE_URL}/history")

            st.success("History cleared successfully.")

            st.rerun()

    # ==========================
    # Display History
    # ==========================
    for item in history:

        with st.expander(
            f"📄 {item['filename']}  |  🎯 ATS Score: {item['ats_score']}%"
        ):

            st.write(f"**Resume Length:** {item['resume_length']} characters")

            st.write("### ✅ Matched Skills")

            if item["matched_skills"]:
                st.success(", ".join(item["matched_skills"]))
            else:
                st.info("No matched skills")

            st.write("### ❌ Missing Skills")

            if item["missing_skills"]:
                st.error(", ".join(item["missing_skills"]))
            else:
                st.success("No missing skills")

            st.write("### 💡 Suggestions")

            for suggestion in item["suggestions"]:
                st.info(suggestion)

            if st.button(
                "🗑 Delete Analysis",
                key=f"delete_{item['id']}",
                width="stretch"
            ):

                delete_response = requests.delete(
                    f"{BASE_URL}/history/{item['id']}"
                )

                if delete_response.status_code == 200:
                    st.success("Analysis deleted successfully.")
                    st.rerun()
                else:
                    st.error("Unable to delete analysis.")

    # ==========================
    # Download CSV
    # ==========================
    data = []

    for item in history:
        data.append({
            "ID": item["id"],
            "Resume": item["filename"],
            "ATS Score": item["ats_score"],
            "Matched Skills": ", ".join(item["matched_skills"]),
            "Missing Skills": ", ".join(item["missing_skills"]),
            "Resume Length": item["resume_length"]
        })

    df = pd.DataFrame(data)

    st.divider()

    st.download_button(
        "📥 Download History CSV",
        df.to_csv(index=False).encode("utf-8"),
        file_name="resume_history.csv",
        mime="text/csv",
        width="stretch"
    )