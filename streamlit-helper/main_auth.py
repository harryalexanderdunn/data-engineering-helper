import streamlit as st
import streamlit_antd_components as sac
from streamlit_oauth import OAuth2Component

from pages import home, camera, chat, cheat_sheet, file_upload, forms, graphs, messages, tables, extras

import os
import base64
import json

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Set page config
st.set_page_config(layout="wide")

# Remove Streamlit's auto sidebar
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# create an OAuth2Component instance
CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', None)
CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', None)
AUTHORIZE_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
REVOKE_ENDPOINT = "https://oauth2.googleapis.com/revoke"
URI=os.getenv('URI', "http://localhost:8501")

if "auth" not in st.session_state:
    # create a button to start the OAuth2 flow
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
    result = oauth2.authorize_button(
        name="Continue with Google",
        icon="https://www.google.com.tw/favicon.ico",
        redirect_uri=f"{URI}/component/streamlit_oauth.authorize_button/index.html",
        scope="https://www.googleapis.com/auth/userinfo.email",
        key="google",
        extras_params={"prompt": "consent", "access_type": "offline"},
        use_container_width=True,
        pkce='S256',
    )
    
    if result:
        # decode the id_token jwt and get the user's email address
        id_token = result["token"]["id_token"]
        # verify the signature is an optional step for security
        payload = id_token.split(".")[1]
        # add padding to the payload if needed
        payload += "=" * (-len(payload) % 4)
        payload = json.loads(base64.b64decode(payload))
        email = payload["email"]
        st.session_state["auth"] = email
        st.session_state["token"] = result["token"]
        st.rerun()
else:
    st.write(f"Signed in as: {st.session_state['auth']}")
    # New Configured Sidebar
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