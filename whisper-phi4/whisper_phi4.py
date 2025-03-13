from ollama import chat
from ollama import ChatResponse
import whisper
import subprocess

def speech_to_text():
    """
    Records audio from microphone and transcribes it to text using Whisper.
    """
    model = whisper.load_model("base")  # You can choose different models like 'small', 'medium', 'large' for better accuracy
    print("Starting recording...")
    try:
        # Record audio using ffmpeg
        subprocess.run(
            ["ffmpeg", "-y", "-f", "avfoundation", "-i", ":0", "output.wav"], # macOS specific, adjust for other OS
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Recording failed: {e}")
        print("Please ensure ffmpeg is installed and configured correctly.")
        return None

    print("Recording finished, transcribing...")
    audio_file = "output.wav"
    result = model.transcribe(audio_file)
    text = result["text"]
    print(f"Whisper transcribed text: {text}")
    return text

if __name__ == "__main__":
    while True:
        print("\nPlease choose the input method:")
        print("1. Voice input (Whisper)")
        print("2. Text input")
        input_choice = input("Please select 1 or 2: ")

        if input_choice == "1":
            content = speech_to_text()
            if not content:
                print("Speech-to-text failed, please try again.")
                continue # Back to input choice
        elif input_choice == "2":
            content = input("You (Text input): ")
        else:
            print("Invalid selection, please try again.")
            continue # Back to input choice

        if content: # Proceed only if content is not None or empty
            response: ChatResponse = chat(model='llama3.2', messages=[
                {
                    'role': 'user',
                    'content': content
                }
            ])
            print(f"Phi-4 response:\n{response.message.content.strip()}") # Added .strip() to remove potential extra spaces