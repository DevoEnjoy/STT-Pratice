#speechReco.py
import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('D:/audio.wav') as source:
    audio = r.record(source, duration=120)
    vToText = r.recognize_google(audio_data=audio, language='ko-KR')
    print(vToText)

