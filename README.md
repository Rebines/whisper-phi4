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

## Setup
### System Environment
#### Python3.11
[Install](https://www.python.org/downloads/release/python-3110/)

```sh
pip install ollama openai-whisper pyttsx3 zhconv wave pyaudio
```

#### Ollama
[Install](https://ollama.com/)

```sh
ollama run phi4
```

#### FFmpeg
The installation process for FFmpeg varies depending on your operating system. Here are the installation steps for Windows, macOS, and Linux:

**Windows:**

1.  **Download FFmpeg:**
    * Visit the official FFmpeg website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
    * Under the Windows icon, choose a suitable build. Typically, builds from "guyan.dev" or "BtbN" are recommended.
    * Download the compressed file (usually a .zip or .7z file).
2.  **Extract the Files:**
    * Extract the downloaded compressed file to your desired installation directory (e.g., C:\ffmpeg).
3.  **Configure Environment Variables:**
    * Open "Control Panel" -> "System and Security" -> "System" -> "Advanced system settings" -> "Environment Variables."
    * In the "System variables" section, find the "Path" variable and click "Edit."
    * Click "New" and add the path to the FFmpeg "bin" folder (e.g., C:\ffmpeg\bin).
    * Click "OK" to save the changes.
4.  **Verify Installation:**
    * Open the command prompt (press Win + R, type "cmd," and press Enter).
    * Type "ffmpeg -version" and press Enter.
    * If the FFmpeg version information is displayed, the installation was successful.

**macOS:**

1.  **Using Homebrew (Recommended):**
    * If you don't have Homebrew installed on your macOS, install it first. You can run the following command in the terminal:
        * `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    * Run the following command in the terminal to install FFmpeg:
        * `brew install ffmpeg`
2.  **Verify Installation:**
    * Type "ffmpeg -version" in the terminal and press Enter.
    * If the FFmpeg version information is displayed, the installation was successful.

**Linux (e.g., Ubuntu):**

1.  **Using the Package Manager:**
    * Open the terminal.
    * Run the following command to update the package list:
        * `sudo apt update`
    * Run the following command to install FFmpeg:
        * `sudo apt install ffmpeg`
2.  **Verify Installation:**
    * Type "ffmpeg -version" in the terminal and press Enter.
    * If the FFmpeg version information is displayed, the installation was successful.

**Important Notes:**

* Ensure you download FFmpeg from the official website or a trusted source.
* After configuring environment variables, you may need to restart your computer or terminal for the changes to take effect.
* Different linux distributions use different package managers, for example fedora uses the "dnf" package manager.
* Choose the correct FFmpeg version for your operating system and needs.

#### Pytorch
Visit [the official website](http://pytorch.org/get-started/locally/), select the corresponding software system and hardware system, and install it according to the official instructions.

#### Whisper
[GitHub](https://github.com/openai/whisper)
```sh
pip install -U openai-whisper
```

### Usage
Download the latest [release](https://github.com/Rebines/whisper-phi4/releases)
run whisper_phi4.py

## Programmatic Options
### Recording duration
The default recording duration is 3 seconds. You can change the recording duration by viewing the source code
### Whisper model
The default Whisper model is Base. You can choose to load the Whisper model you need to use by viewing the source code. The model can be "tiny", "base", "small", "medium", "large", etc., depending on your needs and computing resources. ([Details in the official repository README](https://github.com/openai/whisper#available-models-and-languages))
