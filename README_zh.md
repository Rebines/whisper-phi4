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
#### Python3.11
[下载](https://www.python.org/downloads/release/python-3110/)

```sh
pip install ollama openai-whisper pyttsx3 zhconv wave pyaudio
```

#### Ollama
[下载](https://ollama.com/)

```sh
ollama run phi4
```

#### Whisper
安装FFmpeg的过程会根据您的操作系统而有所不同。以下是Windows、macOS和Linux系统上的安装步骤：

**Windows系统：**

1.  **下载FFmpeg：**
    * 访问FFmpeg官方网站：[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
    * 在Windows图标下方，选择一个合适的构建版本。通常，从“guyan.dev”或“BtbN”下载构建版本。
    * 下载压缩包（通常是.zip或7z格式）。
2.  **解压文件：**
    * 将下载的压缩包解压到您想要安装FFmpeg的目录（例如，C:\ffmpeg）。
3.  **配置环境变量：**
    * 打开“控制面板”->“系统和安全”->“系统”->“高级系统设置”->“环境变量”。
    * 在“系统变量”部分，找到“Path”变量，然后点击“编辑”。
    * 点击“新建”，然后添加FFmpeg的“bin”文件夹的路径（例如，C:\ffmpeg\bin）。
    * 点击“确定”保存更改。
4.  **验证安装：**
    * 打开命令提示符（按下Win + R，输入“cmd”，然后按Enter）。
    * 输入“ffmpeg -version”，然后按Enter。
    * 如果显示FFmpeg的版本信息，则表示安装成功。

**macOS系统：**

1.  **使用Homebrew（推荐）：**
    * 如果您的macOS上没有安装Homebrew，请先安装它。您可以在终端中运行以下命令来安装Homebrew：
        * `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
    * 在终端中运行以下命令来安装FFmpeg：
        * `brew install ffmpeg`
2.  **验证安装：**
    * 在终端中输入“ffmpeg -version”，然后按Enter。
    * 如果显示FFmpeg的版本信息，则表示安装成功。

**Linux系统（以Ubuntu为例）：**

1.  **使用包管理器：**
    * 打开终端。
    * 运行以下命令来更新软件包列表：
        * `sudo apt update`
    * 运行以下命令来安装FFmpeg：
        * `sudo apt install ffmpeg`
2.  **验证安装：**
    * 在终端中输入“ffmpeg -version”，然后按Enter。
    * 如果显示FFmpeg的版本信息，则表示安装成功。

**重要注意事项：**

* 确保从官方网站或可信来源下载FFmpeg。
* 配置环境变量后，可能需要重新启动计算机或终端才能使更改生效。
* 不同的linux系统可能需要使用不同的包管理器，例如在Fedora系统中需要使用“dnf”包管理器。
* 请根据您的操作系统和需求选择合适的FFmpeg版本。
