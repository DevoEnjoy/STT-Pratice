# moviepyUsing.py
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import sys

def get_filename_without_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def get_directory_from_path(file_path):
    return os.path.dirname(file_path)

def merging(video_file_path):

    standard_file_path = get_directory_from_path(video_file_path) + "/" + get_filename_without_extension(video_file_path)[:14]

    # Load video clip
    video_clip = VideoFileClip(standard_file_path + "_video.mp4")

    # Load audio clip
    audio_clip = AudioFileClip(standard_file_path + "_audio.mp3")

    # Set the audio of the video clip to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Write the final video with merged audio to a file
    video_clip.write_videofile(standard_file_path + ".mp4", codec="libx264", audio_codec="aac")

    print("Combining completed!")

# Example usage
#standard_path = "D:/source/new/10월/07"

#merging(
#    standard_path + "/E20201007_00004_video.mp4", standard_path + "/E20201007_00004_audio.mp3", standard_path + "/E20201007_00004.mp4"
#)

video_file = sys.argv[1]

merging(video_file)