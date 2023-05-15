# STT 오디오 파일 전사 프로그램
# 1. 40어절 이상 시 오류 감지
# 2. 마침표 감지

import speech_recognition as sr

def transcribe_audio(audio_file):
    # Initialize the recognizer
    r = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    # Transcribe the audio
    text = r.recognize_google(audio)

    # Split the text into sentences
    sentences = text.split(". ")

    # Transcribe each sentence
    transcriptions = []
    for sentence in sentences:
        # Check if the sentence has more than 40 words
        if len(sentence.split()) > 40:
            raise ValueError("Sentence exceeds maximum word limit of 40 words")

        transcription = r.recognize_google(sr.AudioData(sentence.encode("utf-8"), 16000, 2))
        transcriptions.append(transcription)

    return transcriptions