import streamlit as st

def show():
    st.title(f"Streamlit Chat Functionality")

    with st.expander('Code'):
        st.markdown("""
        ```py
        with st.chat_message("user"):
                st.write("Hello 👋 What is your name?")
            prompt = st.chat_input("Say something to chat with me!")
            if prompt:
                st.write(f"User has sent the following prompt: {prompt}")
                with st.chat_message("user"):
                    st.write(f"Hi {prompt}! Hook me up to NLP so I can chat to you further.")
        ```
        """)

    with st.chat_message("user"):
        st.write("Hello 👋 What is your name?")
    prompt = st.chat_input("Say something to chat with me!")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
        with st.chat_message("user"):
            st.write(f"Hi {prompt}! Hook me up to NLP so I can chat to you further.")


    