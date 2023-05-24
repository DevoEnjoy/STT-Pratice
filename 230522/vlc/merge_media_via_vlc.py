#merge_media_via_vlc.py
import vlc
import os
import sys

def get_filename_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def get_directory_from_path(file_path):
    return os.path.dirname(file_path)

def merging(video_file_path):
    standard_file_name = get_directory_from_path(video_file_path) + "/" + get_filename_without_extension(video_file_path)[:14]

    # VLC 인스턴스 생성
    vlc_instance = vlc.Instance()

    # VLC 미디어 플레이어 생성
    player = vlc_instance.media_player_new()

    # 비디오 파일 로드
    media = vlc_instance.media_new_path(standard_file_name + "_video.mp4")

    # 음성 파일 로드
    audio = vlc_instance.media_new_path(standard_file_name + "_audio.mp3")

    # 비디오 트랙과 음성 파일을 병합하여 출력 파일 생성
    media.add_attribute(audio)

    # 출력 파일 지정
    media.set_mrl(standard_file_name + ".mp4")

    # 비디오 트랙 설정
    player.set_media(media)

    # 출력 파일 재생
    player.play()

    # 재생이 완료될 때까지 대기
    while player.is_playing():
        pass

    # VLC 인스턴스 종료
    vlc_instance.release()

    print("합치기 완료")

def combine_video_audio(video_file, audio_file, output_file):
    # VLC 인스턴스 생성
    vlc_instance = vlc.Instance()

    # VLC 미디어 플레이어 생성
    player = vlc_instance.media_player_new()

    # 비디오 파일 로드
    media = vlc_instance.media_new_path(video_file)

    # 음성 파일 로드
    audio = vlc_instance.media_new_path(audio_file)

    # 비디오 트랙과 음성 파일을 병합하여 출력 파일 생성
    media.add_subtitle(audio)

    # 출력 파일 지정
    media.set_mrl(output_file)

    # 비디오 트랙 설정
    player.set_media(media)

    # 출력 파일 재생
    player.play()

    # 재생이 완료될 때까지 대기
    while player.is_playing():
        pass

    # VLC 인스턴스 종료
    vlc_instance.release()

    print("합치기 완료")


# 합치기 실행
# combine_video_audio("video.mp4", "audio.mp3", "output.mp4")


arg1 = "D:/source/new/10월/20/E20201020_00003_video.mp4"
arg1 = "D:/source/new/10월/21/E20201021_00002_video.mp4"
# 합치기 실행
merging(arg1)

#if __name__ == "__main__":

    # 사용 예시
    #file_name = get_filename_without_extension(file_path)
    #print(file_name)  # 출력: example

    # 합치기 실행
    # combine_video_audio("video.mp4", "audio.mp3", "output.mp4")
