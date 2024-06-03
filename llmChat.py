import streamlit as st
import requests
import re

# Remove emojis from the text
def remove_emoji(text):
    # Define the emoji pattern
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002500-\U00002BEF"  # chinese char
        "\U00002702-\U000027B0"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642" 
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"  # dingbats
        "\u3030"
        "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

# Print Chat conversation with right format
def print_chat_message(message,ChatTTSServer,audio_seed_input,Audio_temp,Top_P,Top_K,Refine_text):
    text = message["content"]
    if message["role"] == "user":
        with st.chat_message("user", avatar="😊"):
            print_txt(text)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            print_txt(text)
            cleartext = remove_emoji(text)
            #res=requests.post('http://127.0.0.1:9966/tts',data={"text":cleartext,"prompt":"","voice":"4099"})
            res = requests.post('http://127.0.0.1:9966/tts', data={
              "text": cleartext,
              "prompt": "",
              "voice": audio_seed_input,
              "temperature": Audio_temp,
              "top_p": Top_P,
              "top_k": Top_K,
              "skip_refine": Refine_text,
              "custom_voice": audio_seed_input
            })
            audio = res.json()
            audioURL = audio["url"]
            st.audio(audioURL, format="audio/mpeg", autoplay=True, loop=False)

# Print LLM content 
def print_txt(text):
    st.write(text)
