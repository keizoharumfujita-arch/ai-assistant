import streamlit as st
import google.generativeai as genai
import PIL.Image

st.set_page_config(page_title="Run AI")
st.title("Run AI")
st.caption("Powered by Keizo Haru")

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Bottom Input Area
col1, col2 = st.columns([1, 10])
with col1:
    uploaded_file = st.file_uploader("Upload", type=['png', 'jpg', 'jpeg'], label_visibility="collapsed")
with col2:
    prompt = st.chat_input("What is on your mind?")

if prompt:
    # 1. Display User Message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 2. Prepare content for Gemini
    content_to_send = [prompt]
    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        content_to_send.append(image)
    
    # 3. Get AI Response
    response = model.generate_content(content_to_send)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()
