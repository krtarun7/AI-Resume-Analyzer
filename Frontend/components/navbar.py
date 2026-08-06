import streamlit as st
from streamlit_option_menu import option_menu


def show_navbar():

    st.markdown("""
    <style>

    .logo{
        color:#22C55E;
        font-size:32px;
        font-weight:700;
    }

    .user{
        text-align:right;
        color:white;
        font-size:15px;
    }

    .user b{
        color:#22C55E;
    }

    div[data-testid="stHorizontalBlock"]{
        align-items:center;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2.8, 5, 2])

    # Logo
    with col1:
        st.markdown(
            '<p class="logo">🤖 AI Resume Analyzer</p>',
            unsafe_allow_html=True
        )

    # Navigation
    with col2:
        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Resume Analyzer",
                "History",
                "Profile"
            ],
            icons=[
                "house-fill",
                "file-earmark-text-fill",
                "clock-history",
                "person-fill"
            ],
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#0E1117",
                },
                "icon": {
                    "color": "#22C55E",
                    "font-size": "18px"
                },
                "nav-link": {
                    "font-size": "16px",
                    "font-weight": "600",
                    "text-align": "center",
                    "margin": "0px 10px",
                    "padding": "10px 18px",
                    "border-radius": "12px",
                    "--hover-color": "#1F2937",
                    "color": "white",
                },
                "nav-link-selected": {
                    "background-color": "#22C55E",
                    "color": "white",
                },
            }
        )

    # User + Logout
    with col3:

        st.markdown(
            f"""
            <div class="user">
                Welcome,<br>
                <b>{st.session_state.get("user_name", "")}</b>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button(
            "🚪 Logout",
            key="navbar_logout",
            use_container_width=True,
        ):
            st.session_state.clear()
            st.rerun()

    st.divider()

    return selected