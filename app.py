import streamlit as st
import google.generativeai as genai
import PIL.Image

st.set_page_config(page_title="Run AI")
st.title("Run AI")
st.caption("Powered by Keizo Haru")

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
# Using the requested model
model = genai.GenerativeModel('models/gemini-3.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Upload Section (Top)
uploaded_file = st.file_uploader("Add an image", type=['png', 'jpg', 'jpeg'])

# History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input (Bottom)
if prompt := st.chat_input("What is on your mind?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    content = [prompt]
    if uploaded_file:
        content.append(PIL.Image.open(uploaded_file))
        st.chat_message("user").image(uploaded_file, width=200)
    
    response = model.generate_content(content)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()
