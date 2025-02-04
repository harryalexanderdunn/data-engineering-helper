import streamlit as st
import streamlit_antd_components as sac
from pages import home, camera, chat, cheat_sheet, file_upload, forms, graphs, messages, tables, extras

# Set page config
st.set_page_config(layout="wide")

# Remove Streamlit's auto sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

with st.sidebar:
    st.image('images/logo_white.png')
    selected = sac.menu([
        sac.MenuItem('Home Page', icon='house-fill'),
        sac.MenuItem('App Cheat Sheet', icon='lightbulb-fill'),
        sac.MenuItem('App Functionality', icon='box-fill', children=[
            sac.MenuItem('File Uploader', icon='cloud-upload-fill'),
            sac.MenuItem('Forms', icon='clipboard-check-fill'),
            sac.MenuItem('Messages', icon='exclamation-triangle-fill'),
            sac.MenuItem('Tables', icon='bar-chart-fill'),
            sac.MenuItem('Charts & Graphs', icon='graph-up'),
            sac.MenuItem('Camera', icon='camera-video-fill'),
            sac.MenuItem('Chatbox', icon='chat-fill')
        ]),
        sac.MenuItem('Third Party Functionality', icon='github'),
        sac.MenuItem(type='divider'),
        sac.MenuItem('Demos', type='group', children=[
            sac.MenuItem('Example one', icon='lightning-fill', href='https://github.com/davidefiocco/streamlit-fastapi-model-serving'),
            sac.MenuItem('Example two', icon='globe', href='https://github.com/graphistry/graph-app-kit/tree/master'),
        ]),
    ], size='lg', color='black')

# Home page
if selected == 'Home Page':
    home.show()

if selected == 'App Cheat Sheet':
    cheat_sheet.show()

if selected == 'File Uploader':
    file_upload.show()

if selected == "Forms":
    forms.show()

if selected == 'Messages':
    messages.show()

if selected == 'Tables':
    tables.show()

if selected == 'Charts & Graphs':
    graphs.show()

if selected == 'Camera':
    camera.show()

if selected == 'Chatbox':
    chat.show()

if selected == 'Third Party Functionality':
    extras.show()