import streamlit as st

def show():
    st.title(f"Streamlit Message Alerts")
    st.info("""Streamlit has a variey of alerting options available. All are simple to add and can be added anywhere in your process.""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.title("Effects")
        balloon = st.button('Balloon effect')
        if balloon:
            st.balloons()
        snow = st.button('Snow effect')
        if snow:
            st.snow()
    
    with col2:
        st.title("Info")
        toast = st.button('Toast Pop up')
        if toast: 
            st.toast('🤓 Hi! How can I help you today?')
    
    with col3:
        st.title("Alerts")
        error = st.button('Error Alert')
        if error: 
            st.error('Error message')
        warning = st.button('Warning Alert')
        if warning: 
            st.warning('Warning message')
        info = st.button('Info Alert')
        if info: 
            st.info('Info message')
        success = st.button('Success Alert')
        if success: 
            st.success('Success message')

    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st

            balloon = st.button('Balloon effect')
            if balloon:
                st.balloons()
            snow = st.button('Snow effect')
            if snow:
                st.snow()
            toast = st.button('Toast Pop up')
            if toast: 
                st.toast('🤓 Hi! How can I help you today?')
            error = st.button('Error Alert')
            if error: 
                st.error('Error message')
            warning = st.button('Warning Alert')
            if warning: 
                st.warning('Warning message')
            info = st.button('Info Alert')
            if info: 
                st.info('Info message')
            success = st.button('Success Alert')
            if success: 
                st.success('Success message')
            ```""")
