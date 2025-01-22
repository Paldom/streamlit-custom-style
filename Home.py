import streamlit as st
from helpers import init_page

st.set_page_config(
    page_title="Streamlit Custom UI Design",
    layout="wide",
)

init_page()

# Main page (landing page) content
st.title("Welcome to the Streamlit Custom UI Design showcase app")
st.write(
    """
    This is the main page. Use the sidebar to navigate to different
    pages showcasing text elements, data display, charts, chat widgets,
    and status messages. You can also customize the look and feel
    with your own CSS right here in the main app file.
    """
)

