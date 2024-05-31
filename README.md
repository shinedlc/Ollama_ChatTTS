# Ollama ChatTTS

This is an extension project bound to the ChatTTS & ChatTTS WebUI & API project. By calling the ChatTTS API interface functionality, it uses Streamlit as the frontend library for the web interface.

Installation and Deployment:

	1.	Install Ollama from http://ollama.com.
	2.	Download the complete branches of ChatTTS + WebUI and the model files from Huggingface: https://huggingface.co/2Noise/ChatTTS.
	3.	Download the core files of this branch, mainly ollamaChatTTS.py, llmChat.py, and voice.py.

Startup Sequence:

	1.	First, start the Ollama local server.
	2.	Start the ChatTTS WebUI by running python app.py.
	3.	Start the Streamlit application by running streamlit run ollamaChatTTS.py.

 ------------------------------------------------

# Ollama ChatTTS 中文说明

这是一个绑定在 ChatTTS & ChatTTS WebUI & API 项目上的延伸项目，通过调用ChatTTS的API接口功能，使用了 Streamlit 作为 web 界面的前端库

![image](./images/screenshot.png?raw=true)

安装部署：
1. 安装 Ollama, http://ollama.com
2. 下载 ChatTTS + Webui 全部分支，以及通过huggingface下载模型文件，https://huggingface.co/2Noise/ChatTTS
3. 下载本分支核心文件，主要是 ollamaChatTTS.py, llmChat.py, voice.py 三个

启动次序：
1. 先启动 Ollama 本地服务器
2. 通过 python app.py 启动 ChatTTS Webui
3. 通过 Streamlit run ollamaChatTTS.py
