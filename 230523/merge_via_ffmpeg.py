#merge_via_ffmpeg.py
import subprocess

def merge_audio_with_video(video_path, audio_path, output_path):
    # ffmpeg 명령어 생성
    cmd = ['ffmpeg', '-i', video_path, '-i', audio_path, '-c:v copy', 'copy', '-c:a copy', 'aac', '-map', '0:v:0', '-map', '1:a:0', output_path]
    
    # ffmpeg 실행
    result = subprocess.run(cmd, capture_output=True)
    print(result.stdout)
    print("-----")
    print(result.stderr)

default_path = 'D:/source/new/10월/07/E20201007_00003'

# 비디오 파일 경로
video_path = default_path + '_video.mp4'
print(video_path)
# 오디오 파일 경로
audio_path = default_path + '_audio.mp3'
print(audio_path)

# 출력 파일 경로
output_path = default_path + '.mp4'
print(output_path)
# 비디오와 오디오 합치기
merge_audio_with_video(video_path, audio_path, output_path)
