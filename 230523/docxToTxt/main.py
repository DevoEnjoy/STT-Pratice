# main.py
from common import *
import firstProcess as first
import secondProcess as second
import thirdProcess as third
import fourthProcess as last
import dayTimeToSeconds as tosec
docx_file = strip_quotes(input("Enter the .docx file path: "))
folder_path = first.run(docx_file, "first")
# docx파일을 단순 txt 파일로 출력
# 폴더 경로 설정까지 작업.
""" 결과 예시

방송일지                                                              2020년 10월 1일


시간	내                        용
09:00	※ 방송시작 ( 위성파 - 수신양호 )
"""
print(f"1차 공정 : .docx파일이 성공적으로 .txt파일로 출력되었습니다. 폴더 경로: {folder_path}")

for file in get_txt_files_in_folder(folder_path):
    print(file)
    second.run(folder_path + "/" + file, 'second')
    delete_file(folder_path, file)
""" 결과 예시
방송일지                                                              2020년 10월 1일
09:00	※ 방송시작 ( 위성파 - 수신양호 )
05	오늘의 순서
"""
print("2차 공정 완료")

for file in get_txt_files_in_folder(folder_path):
    print(file)
    third.run(folder_path + "/" + file, 'third')
    delete_file(folder_path, file)
""" 결과 예시
09:00	※ 방송시작 ( 위성파 - 수신양호 )
09:05	오늘의 순서
"""
print("3차 공정 완료")

""" 출력 예시(두줄로 만들기)
09:00	09:05	※ 방송시작 ( 위성파 - 수신양호 )
09:05	09:12	오늘의 순서
...
22:58	23:03	음악 ( 지새지 말아다오 평양의 밤아 )
23:03	23:03	래일의 순서
"""
"""
for file in get_txt_files_in_folder(folder_path):
    print(file)
    last.run(folder_path + "/" + file)
    delete_file(folder_path, file)

print('4차 공정 완료')
"""

for file in get_txt_files_in_folder(folder_path):
    print(file)
    lastFile = tosec.run(folder_path + "/" + file)
    #lastFile = tosec.run2(folder_path + "/" + file)
    delete_file(folder_path, file)
print("초단위 변환 완료. 마지막 작업파일: " + lastFile)