import streamlit as st
import pandas as pd
import plotly.express as px


def show_ats_chart(history):

    if len(history) == 0:
        st.info("No resume data available.")
        return

    df = pd.DataFrame(history)

    fig = px.line(
        df,
        x=df.index + 1,
        y="ats_score",
        markers=True,
        title="ATS Score Trend"
    )

    fig.update_layout(
        template="plotly_dark",
        height=400,
        xaxis_title="Resume",
        yaxis_title="ATS Score",
        title_x=0.5,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_score_distribution(history):

    if len(history) == 0:
        return

    scores = []

    for item in history:

        score = item["ats_score"]

        if score >= 90:
            scores.append("90-100")

        elif score >= 80:
            scores.append("80-89")

        elif score >= 70:
            scores.append("70-79")

        elif score >= 60:
            scores.append("60-69")

        else:
            scores.append("<60")

    df = pd.DataFrame({
        "Range": scores
    })

    chart = px.pie(
        df,
        names="Range",
        title="ATS Score Distribution"
    )

    chart.update_layout(
        template="plotly_dark",
        height=400,
        title_x=0.5
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )