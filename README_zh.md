<div align="center">
  <h1>whisper-phi4</h1>
  
  [English](README.md) | **简体中文**
</div>

## 特性
### 高效
根据官方数据，Phi4拥有强劲性能的同时仅需更少的性能，效率更高
<img src='https://github.com/user-attachments/assets/f7541460-4176-469e-8f8f-8e673fc59f86'>

### 语音输入
实时音频采样，并通过[**OpenAI Whisper**](https://github.com/openai/whisper)转为文字输入，获取模型文字输出

### 语音输出
通过本地/在线语音合成、输出语音

## 部署
### 系统环境配置
[Python3.11](https://www.python.org/downloads/release/python-3110/)

```sh
pip install ollama openai-whisper pyttsx3 zhconv wave pyaudio
```

[Ollama](https://ollama.com/)

```sh
ollama run phi4
```
