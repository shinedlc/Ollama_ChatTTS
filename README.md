
<div align="center">
</br>
<img src="./images/logo.png" width="400px">
</br>
</div>


中文 ｜ [ENGLISH](./README_EN.md)

Ollama ChatTTS 是一个绑定在 ChatTTS & ChatTTS WebUI & API 项目上的延伸项目，通过调用ChatTTS的API接口功能，使用了 Streamlit 作为 web 界面的前端库

<div align="center">
<img src="./images/screenshot.png" width="600px" align="center">
</div>

## 更新说明:

### 1.0.1 
1. 增加 ChatTTS 设置， 支持更改语音语调，口语化等参数
2. 增加文字输入框，支持文本输入

### 1.0.0
1. 支持语音输入
2. 支持 Ollama 服务器、模型设置
3. 支持说话语种设置（语音输入的语言）



## 安装部署

1. 下载并安装 [Ollama](http://ollama.com)
2. 通过命令行，下载一个模型，在这里可以替换 phi3 为你想要的模型，[模型在这里下载](https://ollama.com/library)
   
   ```bash
   ollama pull phi3
   
4. 下载 ChatTTS 代码， https://github.com/2noise/ChatTTS
5. 通过 [huggingface ](https://huggingface.co/2Noise/ChatTTS) 下载所有模型文件和配置文件，分别放入 asset 和 config 目录
6. 下载 [ChatTTS Webui](https://github.com/jianchang512/ChatTTS-ui/) 分支，放入相同目录
7. 下载本分支核心文件，主要是 ollamaChatTTS.py, llmChat.py, voice.py 三个文件
8. 安装依赖库

   ```bash
   pip install -r requirements.txt

## 启动次序：

1. 先启动 Ollama 本地服务器，在浏览器里输入 http://127.0.0.1:11434 ，看到有一行运行中的文字，确定已运行成功
2. 通过命令行或者 run.bat 启动 ChatTTS Webui，成功后会自动打开 http://127.0.0.1:9966

   ```bash
   python app.py

3. 通过命令行启动 Ollama ChatTTS

   ```bash
   Streamlit run ollamaChatTTS.py

## 项目趋势

[![Star History Chart](https://api.star-history.com/svg?repos=hkgood/Ollama_ChatTTS&type=Date)](https://star-history.com/#hkgood/Ollama_ChatTTS&Date)
