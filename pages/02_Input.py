import streamlit as st
from helpers import init_page

def main():
    init_page()

    st.title("Input Elements")
    st.write("This page demonstrates various input widgets in Streamlit.")

    st.header("Buttons")
    if st.button("Click me! - Secondary by default"):
        st.success("Button clicked!")

    st.button("Primary button", type="primary")
    st.button("Warning button", key="warning")

    st.header("Text Input")
    user_input = st.text_input("Enter some text:")
    st.write(f"You entered: `{user_input}`")

    st.header("Slider")
    slider_val = st.slider("Select a value:", 0, 100, 50)
    st.write(f"Slider value: {slider_val}")

    st.header("Checkbox")
    is_checked = st.checkbox("Check me!")
    if is_checked:
        st.write("Checkbox is checked.")

    st.header("Radio Buttons")
    choice = st.radio("Select an option:", ["Option A", "Option B", "Option C"])
    st.write(f"Your choice: {choice}")

    st.header("Selectbox")
    select_val = st.selectbox("Pick a color:", ["Red", "Green", "Blue"])
    st.write(f"You selected {select_val}")

    st.header("Additional Inputs")

    st.download_button("Download Example", data="Sample content", file_name="example.txt")
    with st.form("example_form"):
        st.write("Form with submit button")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Form submitted!")

    st.markdown("[Open a link](https://example.com)")

    st.color_picker("Pick a color")
    st.multiselect("Pick multiple options", ["Option A", "Option B", "Option C"])
    st.select_slider("Select a range", options=[0, 1, 2, 3, 4], value=2)
    st.number_input("Numeric input", min_value=0, max_value=10, value=5)
    st.date_input("Pick a date")
    st.time_input("Pick a time")
    st.text_area("Enter multiline text")
    # st.camera_input("Take a picture")
    st.file_uploader("Upload a file")

if __name__ == "__main__":
    main()
