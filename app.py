import streamlit as st
from streamlit_mic_recorder import mic_recorder
import google.generativeai as genai

# Paste your API key inside the quotes below
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Using the latest stable model
model = genai.GenerativeModel('gemini-3.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is on your mind?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
import streamlit as st

# 1. Change the page title
st.set_page_config(page_title="Run AI")

# 2. Add the title and the "Powered by" text
st.title("Run AI")
st.caption("Powered by Keizo Haru")
import streamlit as st
from streamlit_mic_recorder import mic_recorder
import google.generativeai as genai

# Setup
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-3.5-flash')

# Page Configuration
st.set_page_config(page_title="Run AI")

# Features
uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image")

# New simple voice recorder
audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)
