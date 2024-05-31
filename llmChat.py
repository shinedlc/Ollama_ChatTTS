import streamlit as st
import requests

# Print Chat conversation with right format
def print_chat_message(message):
    text = message["content"]
    if message["role"] == "user":
        with st.chat_message("user", avatar="😊"):
            print_txt(text)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            print_txt(text)
            res=requests.post('http://127.0.0.1:9966/tts',data={"text":text,"prompt":"","voice":"4099"})
            audio = res.json()
            audioURL = audio["url"]
            st.audio(audioURL, format="audio/mpeg", autoplay=True,loop=False)

# Print LLM content 
def print_txt(text):
    st.write(text)
