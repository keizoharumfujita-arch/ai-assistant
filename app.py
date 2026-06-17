import streamlit as st
import google.generativeai as genai

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

# Using the native chat input with file support
if prompt := st.chat_input("What is on your mind?", accept_files=True):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()
