import streamlit as st
import pandas as pd
import time

def show():
    st.title(f"Streamlit File Uploader")
    st.subheader('Upload a file')
    st.info("""It is very simple to add a file uploader to you application in streamlit.
            The file can be of any type and you can specify what the user can upload and the information stated on the upload button.
            The code in the backend just has to be able to read the file once it is passed in. 
            This means you should be specific about what type of file the user should upload. Error catching is also useful if the user 
            uploads a file incorrectly""")
    uploaded_file = st.file_uploader(label="Choose a csv file", 
                                     type="csv", 
                                     accept_multiple_files=False, 
                                     key=None, 
                                     help="Only csv files can be uploaded here!", 
                                     on_change=None, 
                                     disabled=False, 
                                     label_visibility="visible")
    if uploaded_file:
        with st.status("Processing data..."):
            try:
                st.write("Parsing data...")
                df = pd.read_csv(uploaded_file)
                time.sleep(4)
                st.write("Running data checks...")
                # Add data checks
                time.sleep(2)
                st.write("Transforming data...")
                # Add Transformation
                time.sleep(1)
                st.subheader('DataFrame')
                st.write(df)
                st.subheader('Descriptive Statistics')
                st.write(df.describe())
            except Exception as e:
                st.exception(e)

    with st.expander('Code'):
        st.markdown("""
        ```py
        import streamlit as st
        import pandas as pd
        import time
                    
        uploaded_file = st.file_uploader(label="Choose a csv file", 
                                         type="csv", 
                                         accept_multiple_files=False, 
                                         key=None, 
                                         help="Only csv files can be uploaded here!", 
                                         on_change=None, 
                                         disabled=False, 
                                         label_visibility="visible"
                                        )
        if uploaded_file:
        with st.status("Processing data..."):
            try:
                st.write("Parsing data...")
                df = pd.read_csv(uploaded_file)
                time.sleep(4)
                st.write("Running data checks...")
                # Add data checks
                time.sleep(2)
                st.write("Transforming data...")
                # Add Transformation
                time.sleep(1)
                st.subheader('DataFrame')
                st.write(df)
                st.subheader('Descriptive Statistics')
                st.write(df.describe())
            except Exception as e:
                st.exception(e)

        ```
        """)
