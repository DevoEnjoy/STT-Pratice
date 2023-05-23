#merge_via_vlc
import vlc
import os
import sys

def get_filename_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def get_directory_from_path(file_path):
    return os.path.dirname(file_path)

def merge_audio_with_video(video_file_path):
    # standard_file_name = get_directory_from_path(video_file_path) + '/' + get_filename_without_extension(video_file_path)[:15]
    # print(standard_file_name)
    
    # VLC 미디어 플레이어 인스턴스 생성
    vlc_instance = vlc.Instance()
    
    # 비디오 플레이어 생성
    video_player = vlc_instance.media_player_new()
    
    # 비디오 미디어 생성
    video_media = vlc_instance.media_new_path(video_file_path + '_video.mp4')
    print(video_media)

    # 오디오 미디어 생성
    audio_media = vlc_instance.media_new_path(video_file_path + '_audio.mp3')
    print(audio_media)
    
    # 비디오 트랙 가져오기
    # video_track = video_media.tracks_get()[0]
    
    # 오디오 트랙 가져오기
    # audio_track = audio_media.tracks_get()[0]
    
    # 비디오 트랙을 비디오 플레이어에 추가
    video_player.set_media(video_media)
    video_player.set_media(audio_media)
    
    # 오디오 트랙을 비디오 트랙에 추가
    #video_track.add_slave(vlc.libvlc_media_slave_type_t.libvlc_slave_audio, audio_track)
    
    # 출력 미디어 생성
    output_media = vlc_instance.media_new_path(video_file_path + '.mp4')
    
    # 출력 미디어에 비디오 트랙 추가
    output_media.add_slave(vlc.libvlc_media_slave_type_t.libvlc_slave_audio, video_player)
    
    # 출력 미디어를 재생
    output_player = vlc_instance.media_player_new_from_media(output_media)
    output_player.play()
    
    # 재생이 완료될 때까지 대기
    while output_player.is_playing():
        pass

# 비디오 파일 경로
video_path = 'D:\\source\\new\\10\\07\\E20201007_00010'

# 오디오 파일 경로
# audio_path = input()

# 출력 파일 경로
# output_path = input()

# 비디오에 오디오 추가하여 출력
merge_audio_with_video(video_path)
