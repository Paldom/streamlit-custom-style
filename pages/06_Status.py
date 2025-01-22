import streamlit as st
import time
from helpers import init_page

def main():
    init_page()

    st.title("Status Elements")
    st.write("Showcase how Streamlit can display various status messages and progress bars.")

    st.subheader("Alerts / Toasts")
    st.success("This is a success message!")
    st.info("This is an info message!")
    st.warning("This is a warning message!")
    st.error("This is an error message!")

    st.subheader("Progress Bar")
    progress_bar = st.progress(0)
    for i in range(101):
        time.sleep(0.01)
        progress_bar.progress(i)

    st.subheader("Spinner")
    with st.spinner("Loading..."):
        time.sleep(2)
    st.write("Done!")

if __name__ == "__main__":
    main()
