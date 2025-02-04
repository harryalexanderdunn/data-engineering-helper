import streamlit as st

def show():
    st.title(f"Streamlit Forms & buttons")

    form = st.form('my_form')
    # Input widgets
    check = form.checkbox('Check me out')
    radio = form.radio('Pick one:', ['happy','sad'])
    select = form.selectbox('Select', [2,3,4])
    multi = form.multiselect('Multiselect', [1,2,3])
    slide = form.slider('Slide me', min_value=0, max_value=10)
    slide_select = form.select_slider('Slide to select', options=["good","bad"])
    text = form.text_input('Enter some text')
    num = form.number_input('Enter a number')
    text_area = form.text_area('Area for textual entry')
    date = form.date_input('Date input')
    time = form.time_input('Time entry')
    colour = form.color_picker('Pick a color')
    # Every form must have a submit button
    submitted = form.form_submit_button('Submit')
    
    if submitted:
        st.markdown(f'''
            🚀 form Submitted:
            It was `{check}` that you wanted to check the box because you were `{radio}`.
            You have been `{radio}` `{select}` times.
            Your favourite numbers are: `{multi}` which is a `{slide}` on a scale of 1-10.
            This is a `{slide_select}` choice. Because `{text}`.
            You chose the number `{num}` because `{text_area}`.
            All of this was submitted for `{date}` at `{time}`, with your colour `{colour}`
            ''')
    else:
        st.write('☝️ Submit your form to hear a story!')
    
    with st.expander('Code'):
        st.markdown("""
            ```py
            import streamlit as st
            
            form = st.form('my_form')
            # Input widgets
            check = form.checkbox('Check me out')
            radio = form.radio('Pick one:', ['happy','sad'])
            select = form.selectbox('Select', [2,3,4])
            multi = form.multiselect('Multiselect', [1,2,3])
            slide = form.slider('Slide me', min_value=0, max_value=10)
            slide_select = form.select_slider('Slide to select', options=["good","bad"])
            text = form.text_input('Enter some text')
            num = form.number_input('Enter a number')
            text_area = form.text_area('Area for textual entry')
            date = form.date_input('Date input')
            time = form.time_input('Time entry')
            colour = form.color_picker('Pick a color')
            # Every form must have a submit button
            submitted = form.form_submit_button('Submit')
            ```
            """)
