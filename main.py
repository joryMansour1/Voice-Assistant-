import cohere
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile
import pyttsx3

# إعداد Whisper
whisper_model = whisper.load_model("base")

# إعداد Cohere
co = cohere.Client("###..")  

# تسجيل الصوت
def record_audio(filename="input.wav", duration=5, fs=16000):
    print("🎙️ Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    wavfile.write(filename, fs, recording)
    print("✅ Recording saved to", filename)

# تحويل صوت إلى نص
def speech_to_text(filename="input.wav"):
    print("🔎 Transcribing...")
    result = whisper_model.transcribe(filename)
    print("You :", result["text"])
    return result["text"]

# إرسال النص إلى Cohere
def generate_response(text):
    response = co.chat(
        message=text,
        model="command-r7b-arabic-02-2025",
        preamble="You are a helpful assistant. Answer in less than 15 words."
    )
    print("🤖 :", response.text)
    return response.text

# تحويل النص إلى صوت
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# التجربة الكاملة
def main():
    record_audio()
    text = speech_to_text()
    response = generate_response(text)
    text_to_speech(response)

if __name__ == "__main__":
    main()