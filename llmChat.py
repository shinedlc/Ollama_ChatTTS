import streamlit as st
import requests
import re

# Remove emojis from the text
def remove_emoji(text):
    # Define the emoji pattern
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & pictographs
        "\U0001F680-\U0001F6FF"  # Transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # Flags (iOS)
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\u2600-\u26FF"  # Miscellaneous Symbols
        "\u2700-\u27BF"  # Dingbats
        "\u2300-\u23FF"  # Miscellaneous Technical
        "\u2B50-\u2B55"  # Stars and a few other symbols
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
            print("AI:" + cleartext)
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
            print("Audio:" + res.text)
            audio = res.json()
            if audio["code"] != 0:
                st.error(audio["msg"])
            else:
                audioURL = audio["url"]
                st.audio(audioURL, format="audio/mpeg", autoplay=True, loop=False)

# Print LLM content 
def print_txt(text):
    st.write(text)
