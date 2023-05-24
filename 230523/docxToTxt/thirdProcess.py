# thirdProcess.py
"""
TimetableConverter 클래스는 입력된 시간표를 처리하고 변환하는 역할을 합니다. 클래스 내에는 timetable과 last_hour라는 두 개의 인스턴스 변수가 정의되어 있습니다.

timetable은 입력된 시간표의 내용을 문자열로 저장합니다.
last_hour는 마지막으로 처리된 시간의 시간 부분을 저장합니다.
convert_time() 메서드는 입력된 시간 문자열을 변환하여 24시간 형식(HH:MM)으로 반환합니다.

시간 문자열을 좌우의 공백을 제거합니다.
빈 문자열이면 None을 반환합니다.
시간 문자열에 "시간"이 포함되어 있다면 None을 반환합니다.
시간 문자열에 콜론(:)이 포함되어 있다면 시간과 분으로 분리하여 정수로 변환합니다.
콜론이 없는 경우 시간 문자열의 길이를 확인하고, 길이가 2이면 마지막으로 처리된 시간의 시간 부분을 사용하고, 길이가 5이면 새로운 시간으로 처리합니다.
변환된 시간을 24시간 형식(HH:MM)으로 반환합니다.
simplify_time() 메서드는 시간 문자열을 간략화하여 반환합니다.

시간 문자열의 길이가 3인 경우를 처리합니다.
첫 번째와 두 번째 문자가 같다면, 세 번째 문자부터 끝까지를 반환합니다.
두 번째와 세 번째 문자가 같다면, 처음부터 두 번째 문자까지를 반환합니다.
그 외의 경우에는 원래의 시간 문자열을 반환합니다.
load_timetable() 메서드는 주어진 파일 경로에서 시간표를 읽어 timetable 변수에 저장합니다.

파일 경로에서 따옴표를 제거합니다.
codecs.open()을 사용하여 파일을 열고, UTF-8 인코딩으로 읽어온 내용을 timetable 변수에 저장합니다.
convert_timetable() 메서드는 시간표를 변환하여 새로운 형식으로 반환합니다.

빈 문자열로 초기화된 new_timetable 변수를 생성합니다.
시간표를 줄 단위로 분할한 후, 각 줄을 처리합니다.
탭 문자(\t)로 분리된 부분이 적어도 2개 이상인 경우에만 처리합니다.
시작 시간을 추출하고, convert_time() 메서드를 사용하여 새로운 형식으로 변환합니다. 변환된 값이 None이면 다음 줄을 처리합니다.
마지막으로 처리된 시간의 시간 부분을 업데이트합니다.
시간을 간략화한 후, 새로운 시간과 원래의 나머지 부분을 합쳐서 new_timetable에 추가합니다.
처리된 시간표를 반환합니다.
run() 메서드는 시간표 변환 작업을 실행하는 역할을 합니다.

TimetableConverter 인스턴스를 생성합니다.
파일 경로에서 따옴표를 제거합니다.
load_timetable() 메서드를 사용하여 시간표를 로드합니다.
convert_timetable() 메서드를 사용하여 시간표를 변환합니다.
변환된 시간표를 새로운 파일에 저장합니다.
변환된 시간표가 저장된 파일 경로를 출력합니다.
__name__ == "__main__"을 사용하여 스크립트가 직접 실행되었는지 확인합니다.

사용자로부터 파일 경로를 입력받아 시간표를 변환합니다.
변환된 시간표를 새로운 파일에 저장합니다.
변환된 시간표가 저장된 파일 경로를 출력합니다.
"""
import codecs
import os
from common import *
""" 결과 예시
09:00	※ 방송시작 ( 위성파 - 수신양호 )
09:05	오늘의 순서
"""
class TimetableConverter:
    def __init__(self):
        self.timetable = ""
        self.last_hour = 0

    def convert_time(self, time_str):
        time_str = time_str.strip()
        if not time_str:
            return None
        if '시간' in time_str:
            return None
        if ':' in time_str:
            if len(time_str) != 5:
                return None
            hour = int(time_str[:2])
            minute = int(time_str[3:])
        else:
            if len(time_str) != 2:
                return None
            hour = self.last_hour
            minute = int(time_str[:2])
        return f"{hour:02d}:{minute:02d}"

    def simplify_time(self, time_str):
        if len(time_str) == 3:
            if time_str[0] == time_str[1]:
                return time_str[1:]
            if time_str[1] == time_str[2]:
                return time_str[:2]
        return time_str

    def load_timetable(self, file_path):
        file_path = strip_quotes(file_path)
        with codecs.open(file_path, 'r', encoding='utf-8') as file:
            self.timetable = file.read()

    def convert_timetable(self):
        new_timetable = ""
        lines = self.timetable.split("\n")
        for line in lines:
            parts = line.split("\t")
            if len(parts) >= 2:
                start_time = parts[0]
                new_start_time = self.convert_time(start_time)
                if new_start_time == None:
                    continue
                self.last_hour = int(new_start_time[:2])
                simplified_time = self.simplify_time(new_start_time[3:])
                new_timetable += f"{new_start_time[:3]}{simplified_time}\t{parts[1]}\n"
        return new_timetable
    
def run(file_path, suffix="third"):
    converter = TimetableConverter()
    file_path = strip_quotes(file_path)
    converter.load_timetable(file_path)
    new_timetable = converter.convert_timetable()

    # file_name, file_extension = os.path.splitext(file_path)
    new_file_path = changeSufficWithUnderbar(file_path, suffix)

    with codecs.open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_timetable)

    print(f"Converted timetable saved to: {new_file_path}")

if __name__ == "__main__":
    file_path = input()
    run(file_path=file_path, suffix="third")
    """
    converter = TimetableConverter()
    file_path = strip_quotes(input("Enter the file path: "))
    converter.load_timetable(file_path)
    new_timetable = converter.convert_timetable()

    file_name, file_extension = os.path.splitext(file_path)
    new_file_path = f"{file_name}_new{file_extension}"

    with codecs.open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_timetable)

    print(f"Converted timetable saved to: {new_file_path}")
    """