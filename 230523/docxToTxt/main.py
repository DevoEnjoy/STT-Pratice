# main.py
from common import *
import firstProcess as first
import secondProcess as second
import thirdProcess as third
import lastProcess as last
docx_file = strip_quotes(input("Enter the .docx file path: "))
folder_path = first.run(docx_file, "first")
print(f"1차 공정 : .docx파일이 성공적으로 .txt파일로 출력되었습니다. 폴더 경로: {folder_path}")
for file in get_txt_files_in_folder(folder_path):
    print(file)
    second.TextFileProcessor.run(folder_path + "/" + file, 'second')
    delete_file(folder_path, file)
print("2차 공정 완료")

for file in get_txt_files_in_folder(folder_path):
    print(file)
    third.TimetableConverter.run(folder_path + "/" + file, 'third')
    delete_file(folder_path, file)

print("3차 공정 완료")

for file in get_txt_files_in_folder(folder_path):
    print(file)
    last.lastProcess().run(folder_path + "/" + file)
    delete_file(folder_path, file)

print('마지막 공정 완료')