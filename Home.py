import streamlit as st
from helpers import init_page

init_page(page_title="Streamlit Custom UI Design")

st.title("Welcome to the Streamlit Custom UI Design showcase app")
st.write(
    """
    This is the main page. Use the sidebar to navigate to different
    pages showcasing text elements, data display, charts, chat widgets,
    and status messages.

    Styling is driven primarily by native theme configuration in
    `.streamlit/brand-theme.toml`, with a tiny scoped CSS layer
    for custom component variants.
    """
)
