import streamlit as st


def show_metric_cards(total, avg, best, rating):

    st.markdown("""
    <style>

    .metric-card{
        background:#1E293B;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:1px solid #334155;
        box-shadow:0px 4px 15px rgba(0,0,0,.25);
        transition:0.3s;
    }

    .metric-card:hover{
        transform:translateY(-5px);
        border:1px solid #22C55E;
    }

    .metric-title{
        color:#CBD5E1;
        font-size:16px;
        margin-bottom:10px;
    }

    .metric-value{
        color:#22C55E;
        font-size:34px;
        font-weight:bold;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">📄 Total Resumes</div>
            <div class="metric-value">{total}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">⭐ Average ATS</div>
            <div class="metric-value">{avg}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🏆 Best ATS</div>
            <div class="metric-value">{best}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🤖 AI Rating</div>
            <div class="metric-value">{rating}</div>
        </div>
        """, unsafe_allow_html=True)