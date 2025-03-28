<div align="center">
  <h1>whisper-phi4</h1>
  
  **English** | [简体中文](README_zh.md)
</div>

## Features
### Efficient
According to official data, Phi4 has strong performance while requiring less power and is more efficient.
<img src='https://github.com/user-attachments/assets/f7541460-4176-469e-8f8f-8e673fc59f86'>

### Voice Input
Real-time audio sampling, and converting it into text input through [**OpenAI Whisper**](https://github.com/openai/whisper) to obtain model text output

### Voice Output
Synthesize and output speech locally or online

## Deploy
### System Environment
[Python3.11](https://www.python.org/downloads/release/python-3110/)

```sh
pip install ollama openai-whisper pyttsx3 zhconv wave pyaudio
```

[Ollama](https://ollama.com/)

```sh
ollama run phi4
```

Download the latest release

```sh
python3 whisper_phi4.py
```
