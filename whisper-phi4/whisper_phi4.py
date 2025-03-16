import whisper
import subprocess
import platform
import logging
from ollama import chat
from ollama import ChatResponse

logging.basicConfig(level=logging.INFO)

def record_audio(output_file="output.wav"):
    """
    Records audio from microphone and saves it to a file.
    """
    logging.info("开始录音...")
    try:
        if platform.system() == "Darwin":  # macOS
            subprocess.run(
                ["ffmpeg", "-y", "-f", "avfoundation", "-i", ":0", output_file],
                capture_output=True,
                text=True,
                check=True
            )
        elif platform.system() == "Windows":  # Windows
            subprocess.run(
                ["ffmpeg", "-y", "-f", "dshow", "-i", "audio=Microphone", output_file],
                capture_output=True,
                text=True,
                check=True
            )
        else:  # Linux
            subprocess.run(
                ["ffmpeg", "-y", "-f", "alsa", "-i", "default", output_file],
                capture_output=True,
                text=True,
                check=True
            )
    except subprocess.CalledProcessError as e:
        logging.error(f"录音失败: {e}")
        logging.error("请确保已安装 ffmpeg 并配置正确。")
        return None
    logging.info("录音结束")
    return output_file

def transcribe_audio(audio_file):
    """
    Transcribes audio file to text using Whisper.
    """
    logging.info("转录中...")
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    text = result["text"]
    logging.info(f"Whisper 转录文本: {text}")
    return text

def speech_to_text():
    """
    Records audio from microphone and transcribes it to text using Whisper.
    """
    audio_file = record_audio()
    if audio_file:
        return transcribe_audio(audio_file)
    return None

if __name__ == "__main__":
    while True:
        print("\n请选择输入方式:")
        print("1. 语音输入 (Whisper)")
        print("2. 文本输入")
        input_choice = input("请选择 1 或 2: ")

        if input_choice == "1":
            content = speech_to_text()
            if not content:
                print("语音转文字失败，请重试。")
                continue  # Back to input choice
        elif input_choice == "2":
            content = input("You (文本输入): ")
        else:
            print("无效的选择，请重新输入。")
            continue  # Back to input choice

        if content:  # Proceed only if content is not None or empty
            response: ChatResponse = chat(model='llama3.2', messages=[
                {
                    'role': 'user',
                    'content': content
                }
            ])
            print(f"Ollama 回复:\n{response.message.content.strip()}")  # Added .strip() to remove potential extra spaces