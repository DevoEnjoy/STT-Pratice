# split_video.py
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

# 비디오 파일을 분할 및 경로 이동
# 이동할 경로에 있는 파일명의 특정 문자열에서 비디오를 분할하게 될 시작 시간과 끝 시간 추출
# 이동된 비디오 파일 맨 마지막에 시작 시간과 끝 시간을 초 단위로 자동으로 기입

def cut_video_with_parts(input_file, output_file, start_time, end_time):
    base_path = os.path.dirname(output_file)
    file_name = os.path.splitext(os.path.basename(output_file))[0]
    file_ext = os.path.splitext(os.path.basename(output_file))[1]

    start_time_str = str(start_time).zfill(2) if start_time > 0 else '0'
    end_time_str = str(end_time).zfill(2)

    output_file_with_times = f"{file_name}_{start_time_str}_{end_time_str}{file_ext}"
    output_path = os.path.join(base_path, output_file_with_times)

    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_path)
    print(f"Video cut and saved as '{output_file_with_times}'")

def get_filenames(path):
    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filenames.append(file)
    return filenames

def extract_file_parts(filenames):
    extracted_parts = []
    for filename in filenames:
        part1 = filename[22:27]
        part2 = filename[28:33] 
        extracted_parts.append((part1, part2))
    return extracted_parts

if __name__ == "__main__":
    # 이 경로 내부에 있는 파일명 특정 문자열을 읽습니다.
    directory_path = "D:/데이터작업/1.편성표분할작업/11/04"
    filenames = get_filenames(directory_path)
    extracted_parts = extract_file_parts(filenames)

    for part1, part2 in extracted_parts:
        start_time = int(part1)
        end_time = int(part2)
        # 이동하려는 비디오 파일 경로를 입력하세요.
        input_file = "D:/데이터작업/0.문장분할작업/11/05/E20201105_00002_video.mp4" 
        # 비디오 파일을 이동시킬 경로를 입력하세요. 
        output_file = f"D:/데이터작업/1.편성표분할작업/11/04/E20201104_00002_video.mp4"  
        cut_video_with_parts(input_file, output_file, start_time, end_time)