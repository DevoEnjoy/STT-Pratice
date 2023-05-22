#unlock_docx.py
import os
import win32com.client as win32
from docx import Document

def decrypt_protected_docx(encrypted_file_path, password):
    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(encrypted_file_path, False, False, False, password)
    
    original_file_name = os.path.splitext(encrypted_file_path)[0]
    output_file_path = original_file_name + "_unlocked.docx"
    
    doc.SaveAs2(output_file_path, FileFormat=16, Password="")  # FileFormat 16은 .docx 형식을 의미합니다.
    doc.Close()
    word.Quit()
    
    return output_file_path
if __name__ == "__main__":
    # 암호화된 .docx 파일 경로
    encrypted_file_path = 'C:/Users/user/Desktop/list/202009.docx'

    # 암호
    password = "fpdlqmffld"

    # 암호를 푼 .docx 파일 출력 경로
    output_file_path = decrypt_protected_docx(encrypted_file_path, password)

    print("암호가 풀린 파일이 저장되었습니다:", output_file_path)
