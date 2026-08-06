import streamlit as st

from components.navbar import show_navbar

from pages.dashboard import show_dashboard
from pages.analyzer import show_analyzer
from pages.history import show_history
from pages.profile import show_profile
from pages.login import show_login
from pages.signup import show_signup
from pages.forgot_password import show_forgot_password


# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =====================================================
# Session State
# =====================================================

defaults = {
    "logged_in": False,
    "user_name": "",
    "user_email": "",
    "token": "",
    "show_forgot": False,
    "auth_page": "Login"
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# Global CSS
# =====================================================

st.markdown("""
<style>

/* Hide Streamlit Sidebar */
[data-testid="stSidebar"]{
    display:none;
}

[data-testid="collapsedControl"]{
    display:none;
}

/* Background */
.stApp{
    background:#0F172A;
}

/* Main Container */
.block-container{
    padding-top:1rem;
    padding-left:3rem;
    padding-right:3rem;
    max-width:1500px;
}

/* Remove top padding */
header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# Authentication
# =====================================================

if not st.session_state.logged_in:

    if st.session_state.show_forgot:

        show_forgot_password()

    else:

        auth = st.segmented_control(
            "",
            ["Login", "Signup"],
            default=st.session_state.auth_page
        )

        st.session_state.auth_page = auth

        st.write("")

        if auth == "Login":
            show_login()
        else:
            show_signup()

    st.stop()


# =====================================================
# Navbar
# =====================================================

selected = show_navbar()


# =====================================================
# Routing
# =====================================================

pages = {
    "Dashboard": show_dashboard,
    "Resume Analyzer": show_analyzer,
    "History": show_history,
    "Profile": show_profile,
}

pages[selected]()