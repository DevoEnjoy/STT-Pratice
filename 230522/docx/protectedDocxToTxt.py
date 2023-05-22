#protectedDocxToTxt.py
import win32com.client as win32
from docx import Document

def extract_text_from_protected_docx(docx_file_path, password, output_file_path):
    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(docx_file_path, False, False, False, password)
    
    paragraphs = doc.Content.Paragraphs
    text_data = [paragraph.Range.Text for paragraph in paragraphs]
    text = '\n'.join(text_data)
    
    doc.Close(False)
    word.Quit()
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

if __name__ == "__main__":
    # 암호가 걸린 .docx 파일 경로
    docx_file_path = 'D:/202009list.docx'

    # 문서 암호
    password = input("암호를 입력하세요: ")

    # 텍스트를 추출하여 저장할 파일 경로
    output_file_path = 'D:/output.txt'
    print("loading...")
    # 암호가 걸린 .docx 파일 열기 및 텍스트 추출하여 파일로 저장
    extract_text_from_protected_docx(docx_file_path, password, output_file_path)