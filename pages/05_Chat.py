import streamlit as st
from helpers import init_page

def main():
    init_page()

    st.title("Chat Elements")
    st.write("Demonstrates chat-like elements (text input, st.chat, etc.)")

    st.write("**Note**: The built-in Chat interface is in experimental stages in some Streamlit versions.")

    # Example chat-like interface:
    # st.chat_message("Hello, how can I help you today?")

    st.subheader("User Chat Simulation")
    placeholder = st.empty()
    user_input = st.text_input("Send a message:")
    if user_input:
        placeholder.write(f"**User**: {user_input}")
        # You can add a response logic from an LLM or your own function
        placeholder.write("**App**: This is a mock response.")

    st.write("_Extend this section with your own chat system or AI integration._")

if __name__ == "__main__":
    main()
