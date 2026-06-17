import streamlit as st
import google.generativeai as genai

# Page Setup
st.set_page_config(page_title="Run AI")
st.title("Run AI")
st.caption("Powered by Keizo Haru")

# Configuration
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-3.5-flash')

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Bottom Input Area
with st.container():
    col1, col2 = st.columns([1, 10])
    with col1:
        uploaded_file = st.file_uploader("Upload", type=['png', 'jpg', 'jpeg', 'pdf', 'txt'], label_visibility="collapsed")
    with col2:
        prompt = st.chat_input("What is on your mind?")

# Process Input
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()
