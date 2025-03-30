from ollama import chat
from ollama import ChatResponse
import whisper
import zhconv
import msvcrt  # 用于监听键盘输入，暂停程序运行，等待用户按键继续
import wave  # 使用wave库可读、写wav类型的音频文件
import pyaudio  # 使用pyaudio库可以进行录音，播放，生成wav文件
import pyttsx3  # 使用pyttsx3库可以将文本转换为语音

def record(time):  # 录音程序
    # 定义数据流块
    CHUNK = 1024  # 音频帧率（也就是每次读取的数据是多少，默认1024）
    FORMAT = pyaudio.paInt16  # 采样时生成wav文件正常格式
    CHANNELS = 1  # 音轨数（每条音轨定义了该条音轨的属性,如音轨的音色、音色库、通道数、输入/输出端口、音量等。可以多个音轨，不唯一）
    RATE = 16000  # 采样率（即每秒采样多少数据）
    RECORD_SECONDS = time  # 录音时间
    WAVE_OUTPUT_FILENAME = "./aout.wav"  # 保存音频路径
    p = pyaudio.PyAudio()  # 创建PyAudio对象
    stream = p.open(format=FORMAT,  # 采样生成wav文件的正常格式
                    channels=CHANNELS,  # 音轨数
                    rate=RATE,  # 采样率
                    input=True,  # Ture代表这是一条输入流，False代表这不是输入流
                    frames_per_buffer=CHUNK)  # 每个缓冲多少帧
    print("* recording")  # 开始录音标志
    frames = []  # 定义frames为一个空列表
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):  # 计算要读多少次，每秒的采样率/每次读多少数据*录音时间=需要读多少次
        data = stream.read(CHUNK)  # 每次读chunk个数据
        frames.append(data)  # 将读出的数据保存到列表中
    print("* done recording")  # 结束录音标志

    stream.stop_stream()  # 停止输入流
    stream.close()  # 关闭输入流
    p.terminate()  # 终止pyaudio

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')  # 以’wb‘二进制流写的方式打开一个文件
    wf.setnchannels(CHANNELS)  # 设置音轨数
    wf.setsampwidth(p.get_sample_size(FORMAT))  # 设置采样点数据的格式，和FOMART保持一致
    wf.setframerate(RATE)  # 设置采样率与RATE要一致
    wf.writeframes(b''.join(frames))  # 将声音数据写入文件
    wf.close()  # 数据流保存完，关闭文件

    # 主程序循环，持续监听用户输入并进行处理
try:
    while True:
        pass
        if __name__ == '__main__':
            model = whisper.load_model("base")#在这里加载你需要使用的 Whisper 模型，模型可以是 "tiny", "base", "small", "medium", "large" 等等，根据你的需求和计算资源来选择。
            record(3)  # 定义录音时间，单位/s
            result = model.transcribe("aout.wav")
            s = result["text"]
            content = zhconv.convert(s, 'zh-cn')
            print(content)
            response: ChatResponse = chat(model='phi4', messages=[       #在“model=”后面输入你的语言大模型名称
                        {
                            'role': 'user',
                            'content': content
                        }
                    ])
            print(f"Ollama 回复:\n{response.message.content.strip()}")  # Added .strip() to remove potential extra spaces
            pyttsx3.speak(response.message.content.strip())  # Added .strip() to remove potential extra spaces
            print("Press Enter to continue... (Press Ctrl+C to exit)")
            msvcrt.getch()  # 暂停程序运行，等待用户按键继续，这里使用了msvcrt库中的getch()函数来实现
    # 语音回复
except KeyboardInterrupt:
    print("\n程序已退出")


 
