import streamlit as st
import random
#import time

import ollama as ol
from voice import record_voice
from llmChat import print_chat_message
import requests

st.header(':rainbow[:speech_balloon: Ollama V-Chat]')

tap_chat, tap_setup= st.tabs(
    ["Chat", "Setup"]
)

# Setup CV2 and camera
#camera = cv2.VideoCapture(0)

# User Language selection
def language_selector():
    lang_options = ["ar", "de", "en", "es", "fr", "it", "ja", "nl", "pl", "pt", "ru", "zh"]
    with tap_setup:
        return st.selectbox("Language", ["zh"] + lang_options)

# Ollama Model selection
def OllamaModel():
    ollama_models = [m['name'] for m in ol.list()['models']]
    with tap_setup:
        return st.selectbox("Ollama Moldes", ollama_models)

def OllamaServer():
    OllamaServer = st.text_input("Ollama Server URL", "http://127.0.0.1:11434")

def main():
    with tap_setup:        
        model = OllamaModel()
        

    with tap_chat:
        question = record_voice(language=language_selector())
        with st.container(height=500, border=True):
            # init chat history for a model
            if "chat_history" not in st.session_state:
                st.session_state.chat_history = {}
            if model not in st.session_state.chat_history:
                st.session_state.chat_history[model] = []
            chat_history = st.session_state.chat_history[model]

            # print conversation history
            for message in chat_history: print_chat_message(message)

            if question:
                user_message = {"role": "user", "content": question}
                print_chat_message(user_message)
                chat_history.append(user_message)
                response = ol.chat(model=model, messages=chat_history)
                answer = response['message']['content']
                ai_message = {"role": "assistant", "content": answer}
                print_chat_message(ai_message)
                chat_history.append(ai_message)

                # truncate chat history to keep 20 messages max
                if len(chat_history) > 20:
                    chat_history = chat_history[-20:]
                
                # update chat history
                st.session_state.chat_history[model] = chat_history


if __name__ == "__main__":
    main()
