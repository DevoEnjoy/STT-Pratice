import codecs
from common import strip_quotes

def convert_time(time_str, last_hour):
    if len(time_str) == 5:
        hour = int(time_str[:2])
        minute = int(time_str[3:])
    else:
        hour = last_hour
        minute = int(time_str.strip()) if time_str.strip() else 0
    return f"{hour:02d}:{minute:02d}"

def simplify_time(time_str):
    if len(time_str) == 3:
        if time_str[0] == time_str[1]:
            return time_str[1:]
        if time_str[1] == time_str[2]:
            return time_str[:2]
    return time_str

# 파일 경로 입력 받기
file_path = strip_quotes(input("Enter the file path: "))

# 파일로부터 기존의 방송시간표 읽어오기
with codecs.open(file_path, 'r', encoding='utf-8') as file:
    timetable = file.read()

# 새로운 방송시간표 작성
new_timetable = ""
last_hour = 0
lines = timetable.split("\n")
for line in lines:
    parts = line.split("\t")
    if len(parts) >= 2:
        start_time = parts[0]
        new_start_time = convert_time(start_time, last_hour)
        last_hour = int(new_start_time[:2])
        simplified_time = simplify_time(new_start_time[3:])
        new_timetable += f"{new_start_time[:3]}{simplified_time}\t{parts[1]}\n"

# 결과 출력
print(new_timetable)