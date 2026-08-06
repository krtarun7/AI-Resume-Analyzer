import streamlit as st
from streamlit_option_menu import option_menu


def show_sidebar():

    with st.sidebar:

        # Logo
        st.markdown(
            """
            <div style="text-align:center;">
                <h2 style="color:#4CAF50;">
                    📄 AI Resume Analyzer
                </h2>
                <p style="color:gray;">
                    AI Powered ATS Checker
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # User Details
        st.markdown("### 👤 Logged In")

        st.write(f"**{st.session_state.get('user_name','User')}**")

        st.caption(
            st.session_state.get(
                "user_email",
                ""
            )
        )

        st.divider()

        # Navigation
        selected = option_menu(
            menu_title="Navigation",

            options=[
                "Dashboard",
                "Resume Analyzer",
                "History",
                "Profile"
            ],

            icons=[
                "speedometer2",
                "file-earmark-text",
                "clock-history",
                "person-circle"
            ],

            menu_icon="cast",

            default_index=0,

            styles={

                "container": {
                    "padding": "8px",
                    "background-color": "#111827"
                },

                "icon": {
                    "color": "#4CAF50",
                    "font-size": "18px"
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#262730",
                    "border-radius": "8px",
                },

                "nav-link-selected": {
                    "background-color": "#4CAF50",
                    "color": "white",
                },

            }
        )

        st.divider()

        st.caption("🚀 AI Resume Analyzer v1.0")

    return selected