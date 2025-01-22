import streamlit as st
import pathlib

# Function to load CSS from the 'assets' folder
# Based on https://github.com/Sven-Bo/streamit-css-styling-demo
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def init_page():
    # Load the external CSS
    css_path = pathlib.Path("assets/styles.css")
    load_css(css_path)

    # Set logo and sidebar
    st.logo("images/logo.svg", icon_image="images/logo_closed.svg")
    st.sidebar.markdown("Hi!")