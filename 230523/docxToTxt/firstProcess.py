# firstProcess.py
# docx파일을 단순 txt 파일로 출력
# 폴더 경로 설정까지 작업.
""" 결과 예시

방송일지                                                              2020년 10월 1일


시간	내                        용
09:00	※ 방송시작 ( 위성파 - 수신양호 )
"""
from docx import Document
import os
from common import strip_quotes

def read_tables_from_docx(file_path):
    doc = Document(file_path)
    tables = []
    current_table = []
    for table in doc.tables:
        rows = []
        for row in table.rows:
            if len(row.cells) >= 2:
                cells = [row.cells[0].text, row.cells[1].text]
                rows.append(cells)
            else:
                rows.append([cell.text for cell in row.cells])
                if any("방송일지" in cell.text for cell in row.cells):
                    if current_table:
                        tables.append(current_table)
                    current_table = []
        current_table.append(rows)
    tables.append(current_table)
    return tables

def write_tables_to_txt(tables, file_path, suffix="first"):
    file_directory, file_name = os.path.split(file_path)
    folder_name = os.path.splitext(file_name)[0]

    # 경로설정 : 기본경로/2020/09/최종출력물
    new_folder_path = os.path.join(file_directory, folder_name[:4], folder_name[4:])
    os.makedirs(new_folder_path, exist_ok=True)

    # 파일명으로 삼을 행의 정보를 구분할 키워드
    keyword = "방송일지"
    for table in tables:
        for rows in table:
            for row in rows:
                if any(keyword in cell for cell in row):
                    for cell in row:
                        if keyword in cell:
                            date_string = cell.split(keyword)[1].strip()
                            txt_file = os.path.join(new_folder_path, f'{date_string}_{suffix}.txt')
                            with open(txt_file, 'w', encoding='utf-8') as file:
                                for rows in table:
                                    file.write("\n")
                                    for row in rows:
                                        if len(row) == 2:
                                            row_text = '\t'.join(row)
                                        else:
                                            row_text = '\t'.join(row)
                                        file.write(row_text + '\n')
                                    file.write('\n')
                    break

    return new_folder_path

def run(docx_file, suffix):
    return write_tables_to_txt(read_tables_from_docx(docx_file), docx_file, suffix)

if __name__ == "__main__":
    docx_file = strip_quotes(input("Enter the .docx file path: "))
    output_folder = write_tables_to_txt(read_tables_from_docx(docx_file), docx_file)
    print(f"표가 성공적으로 출력되었습니다. 폴더 경로: {output_folder}")
