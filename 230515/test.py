#test.py
import os
import time
import speech_recognition as sr
from pydub import AudioSegment

# 폴더 경로
folder_path = "D:/"

# Recognizer 객체 생성
rec = sr.Recognizer()

# 오디오 스트림을 백그라운드에서 계속 수신하면서 음성 인식을 수행
def recognize_speech(rec, audio):
    try:
        # 시작 시간 기록
        start_time = time.time()

        # 오디오 스트림에서 음성 인식 수행
        text = rec.recognize_google(audio, language='ko-KR')

        # 종료 시간 기록
        end_time = time.time()

        # 추출된 텍스트, 시작 시간, 종료 시간 리스트에 추가
        text_list.append(text)
        start_time_list.append(start_time)
        end_time_list.append(end_time)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# 폴더 내에 있는 모든 mp3 파일에 대해 작업 수행
for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        print("Processing", filename)

        # 텍스트와 발화 시간을 기록할 리스트 초기화
        text_list = []
        start_time_list = []
        end_time_list = []

        # MP3 파일을 WAV 파일로 변환하여 저장
        mp3_file = os.path.join(folder_path, filename)
        wav_file = os.path.splitext(mp3_file)[0] + ".wav"
        audio = AudioSegment.from_mp3(mp3_file)
        audio.export(wav_file, format="wav")

        # 오디오 파일 불러오기
        r = sr.AudioFile(wav_file)

        # 오디오 스트림을 백그라운드에서 수신하면서 음성 인식 수행
        with r as source:
            audio = rec.listen_in_background(source, recognize_speech)
            input("Press Enter to stop recording...")

        # 수신 중인 오디오 스트림 정지
        audio()

        # SRT 파일 생성
        output_filename = os.path.splitext(filename)[0] + ".srt"
        with open(output_filename, "w") as f:
            for i in range(len(text_list)):
                start_time = start_time_list[i]
                end_time = end_time_list[i]
                text = text_list[i]

                # SRT 파일 형식으로 출력
                f.write(str(i+1) + "\n")
                f.write(time.strftime("%H:%M:%S", time.gmtime(start_time)) + ",000 --> " + time.strftime("%H:%M:%S", time.gmtime(end_time)) + ",000\n")
                f.write(text + "\n")
                f.write("\n")

        print("Saved SRT file as", output_filename)

        # WAV 파일 삭제
        os.remove(wav_file)