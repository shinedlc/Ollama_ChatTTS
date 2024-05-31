#import os
#import sys
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')
#sys.path.append(os.getcwd())
import scipy

import streamlit as st
import re
import requests
from streamlit_mic_recorder import speech_to_text

import ChatTTS
from IPython.display import Audio

chat = ChatTTS.Chat()
chat.load_models()

PATH = 'chattts.wav'

# Record voice base on you lang
def record_voice(language="zh"):
    state = st.session_state
    if "text_received" not in state:
        state.text_received = []

    text = speech_to_text(
        start_prompt="Click to speak",
        stop_prompt="Stop recording",
        language=language,
        use_container_width=True,
        just_once=True,
    )

    if text:
        state.text_received.append(text)

    result = ""
    for text in state.text_received:
        result += text

    state.text_received = []

    return result if result else None

# Save Audio to Mp3
def saveFile(res):
    contentType = res.headers['Content-Type']
    if 'audio' in contentType:
        fo = open(PATH, 'wb')
        fo.write(res.content)
        fo.close()
        print('save file path: ' + PATH)
    else:
        print(str(res.content, 'utf-8'))


# Convert text to audio
def createRequest(text):
    wavs = chat.infer(text, use_decoder=True)
    Audio(wavs[0], rate=24_000, autoplay=True)
    scipy.io.wavfile.write(filename = "./chattts.wav", rate = 24_000, data = wavs[0].T)

def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)

