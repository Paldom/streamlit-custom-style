import streamlit as st
from helpers import init_page

init_page(page_title="Input Elements")

st.title("Input Elements")
st.write("This page demonstrates various input widgets in Streamlit.")

st.header("Buttons")
st.write("Streamlit supports `primary`, `secondary`, and `tertiary` button types natively.")

col1, col2, col3 = st.columns(3)
with col1:
    st.button("Primary", type="primary")
with col2:
    st.button("Secondary", type="secondary")
with col3:
    st.button("Tertiary", type="tertiary")

st.write("Additional keyed variants are styled via scoped CSS (`.st-key-*`):")

col1, col2, col3 = st.columns(3)
with col1:
    st.button("Warning", key="warning")
with col2:
    st.button("Success", key="success")
with col3:
    st.button("Outline", key="outline")

st.header("Card Container")
st.write("Use a keyed container for card-like wrappers:")
with st.container(key="card"):
    st.subheader("Card example")
    st.write("This container is styled with `.st-key-card` in the CSS.")

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

st.header("Tabs and Expander")
tab1, tab2 = st.tabs(["Tab One", "Tab Two"])
with tab1:
    st.write("Content inside Tab One. Borders and radius follow theme config.")
with tab2:
    st.write("Content inside Tab Two.")

with st.expander("Click to expand"):
    st.write("Expander content. Styled by the native theme.")

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
st.file_uploader("Upload a file")
