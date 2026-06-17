import streamlit as st
import google.generativeai as genai
import PIL.Image

st.set_page_config(page_title="Run AI")
st.title("Run AI")
st.caption("Powered by Keizo Haru")

# Upload Section (At the top, no overlap)
uploaded_file = st.file_uploader("Upload an image for the AI to analyze", type=['png', 'jpg', 'jpeg'])

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input (Fixed at the bottom)
if prompt := st.chat_input("What is on your mind?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    content_to_send = [prompt]
    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        content_to_send.append(image)
        # Show image in chat
        st.chat_message("user").image(image, caption="Uploaded Image")
    
    response = model.generate_content(content_to_send)
    
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()
