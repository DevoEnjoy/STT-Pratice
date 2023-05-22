#unlock_and_save.py
import os
import win32com.client as win32
from docx import Document

def decrypt_and_save_docx(encrypted_file_path, password, output_file_path):
    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(encrypted_file_path, False, False, False, password)

    doc.SaveAs2(output_file_path, FileFormat=16, Password="")
    doc.Close()
    word.Quit()

if __name__ == "__main__":
    # 암호화된 .docx 파일 경로
    encrypted_file_path = 'C:/Users/user/Desktop/list/202009.docx'

    # 암호
    password = "fpdlqmffld"

    # 암호를 푼 .docx 파일 출력 경로
    unlocked_file_path = 'C:/Users/user/Desktop/list/202009_unlocked.docx'

    # 암호가 풀린 파일 생성
    decrypt_and_save_docx(encrypted_file_path, password, unlocked_file_path)
    print("암호가 풀린 파일이 저장되었습니다:", unlocked_file_path)
