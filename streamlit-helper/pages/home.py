import streamlit as st

def show():
    st.title(f"Home Page :house:")

    with st.expander('Streamlit Links & Pages'):
        st.write('This app shows the various ways on how you can layout your Streamlit app.')
        st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

    