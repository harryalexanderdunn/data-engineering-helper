import streamlit as st

def show():
    st.title(f"Streamlit Camera Functionality")

    camera = st.checkbox('Toggle Camera Functionality')

    if camera:
        st.header("Camera ON! 😎")
        picture = st.camera_input("Take a picture")
        if picture:
            st.image(picture)
            bytes_data = picture.getvalue()
            st.write(type(bytes_data))
    else:
        st.header("Camera OFF! 🙅‍♂️")

    with st.expander('Code'):
        st.markdown("""
        ```py
        picture = st.camera_input("Take a picture")

        if picture:
            st.image(picture)
            bytes_data = picture.getvalue()
            st.write(type(bytes_data))
        ```
        """)

