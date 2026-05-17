import streamlit as st
from helpers import init_page

init_page(page_title="Status Elements")

st.title("Status Elements")
st.write("Showcase how Streamlit can display various status messages and progress bars.")

st.subheader("Alerts / Toasts")
st.success("This is a success message!")
st.info("This is an info message!")
st.warning("This is a warning message!")
st.error("This is an error message!")

st.subheader("Progress Bar")
st.progress(75)

st.subheader("Spinner")
st.write("Done!")
