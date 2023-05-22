# -*- coding: utf-8 -*-
from docx import Document

def read_table_from_docx(docx_file_path):
    doc = Document(docx_file_path)
    tables = doc.tables
    output = []

    for table in tables:
        for row in table.rows:
            row_data = []
            for cell in row.cells:
                row_data.append(cell.text)
            output.append('\t'.join(row_data))

    return '\n'.join(output)

def write_to_text_file(docx_file_path, output_txt_file_path):
    with open(output_txt_file_path, 'w', -1, 'utf-8') as file:
        file.write(read_table_from_docx(docx_file_path))
if __name__ == "__main__":
    # .docx 파일 경로(비번 없어야 함)
    docx_file = 'D:/practicePlace/workplace/202009list.docx'

    # 텍스트 파일로 출력할 경로와 파일 이름
    output_file = 'D:/output.txt'

    # 텍스트 파일로 출력
    write_to_text_file(output_file, docx_file)
