# split_video2.py
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from common import *
class videoSpliter:

    def __init__(self) -> None:
        self.times = []
        self.contents = []

    def split_line_info(self, filename):
        filename = strip_quotes(filename)
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    line_info = line.split('\t')
                    time = line_info[0]
                    content = line_info[1]
                    self.times.append(time)
                    self.contents.append(content)

def cut_video(input_file, output_file, start_time, end_time, content):
    start_time = int(start_time)
    end_time = int(end_time)
    if start_time == end_time:
        print(f"skip {start_time}")
        return
    base_path = os.path.dirname(output_file)
    file_name = os.path.splitext(os.path.basename(output_file))[0]
    file_ext = os.path.splitext(os.path.basename(output_file))[1]
    
    start_time_str = str(start_time).zfill(5)
    end_time_str = str(end_time).zfill(5)
    if '음악' in content or '만화' in content or '보도시작' in content or '보도종료' in content or '명언' in content:
        print("skip " + content)
        return
    output_file_with_times = f"{file_name}_{start_time_str}_{end_time_str}_{content}{file_ext}"
    output_path = os.path.join(base_path, output_file_with_times)
    
    ffmpeg_extract_subclip(input_file, int(start_time), int(end_time), targetname=output_path)
    print(f"Video cut and saved as '{output_file_with_times}'")

if __name__ == "__main__":
    # Example usage
    input_file = input("작업할 영상 파일.mp4 : ")      # Replace with the path to your input video file
    #output_file = "D:/데이터작업/1.편성표분할작업/11/04/E20201104_00002_video.mp4"    # Replace with the desired output file path
    input_txt = input("적용할 편성표.txt : ")
    obj = videoSpliter()
    obj.split_line_info(input_txt)
    print(obj.times[0])
    origin_start = obj.times[0]
    # output_file = input_file.replace('.txt', '_1.txt')
    cut_video(input_file, input_file, 0, origin_start, obj.contents[0])
    i = 1
    for i in range(len(obj.times)):
        if i+1 == len(obj.times):
            start_time = obj.times[i]                      # Replace with the start time in seconds
            end_time = obj.times[i]                      # Replace with the end time in seconds
        else:
            start_time = obj.times[i-1]                      # Replace with the start time in seconds
            end_time = obj.times[i]                      # Replace with the end time in seconds
            
        number = i+1
        if int(start_time) > int(end_time):
            continue
        cut_video(input_file, input_file, start_time, end_time, obj.contents[i])

