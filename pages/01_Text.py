import streamlit as st
from helpers import init_page

def main():
    init_page()

    st.title("Text Elements")
    st.write("This page demonstrates various text/typography elements in Streamlit.")

    st.header("Headers and Subheaders")
    st.subheader("Subheader Example")
    st.markdown("**Markdown** _formatting_ example with inline `code`.")
    st.caption("Caption text can be used for small notes.")

    st.divider()
    st.text("This is a plain text example.")
    with st.echo():
        st.write("This code is shown because of st.echo()")

    st.header("Other Text Elements")
    st.code("print('Hello, world!')", language="python")
    st.latex(r"""\frac{n!}{k!(n-k)!}""")

if __name__ == "__main__":
    main()
