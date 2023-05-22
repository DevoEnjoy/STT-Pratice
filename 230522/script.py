from moviepy.editor import VideoFileClip, AudioFileClip
import os
import sys


def get_filename_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def get_directory_from_path(file_path):
    return os.path.dirname(file_path)


def merging(video_file_path):
    standard_file_path = (
        get_directory_from_path(video_file_path)
        + "\\"
        + get_filename_without_extension(video_file_path)[:14]
    )
    video_clip = VideoFileClip(standard_file_path + "_video.mp4")
    audio_clip = AudioFileClip(standard_file_path + "_audio.mp3")
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(
        standard_file_path + ".mp4", codec="libx264", audio_codec="aac"
    )
    print("Combining completed!")

merging(sys.argv[1])
