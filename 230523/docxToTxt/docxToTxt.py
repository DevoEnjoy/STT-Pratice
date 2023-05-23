from docx import Document

def read_tables_from_docx(file_path):
    doc = Document(file_path)
    tables = []
    current_table = []
    for table in doc.tables:
        rows = []
        for row in table.rows:
            # 행에 셀이 있는 경우에는 셀의 데이터를 가져오고,
            # 행에 셀이 없는 경우에는 행 전체의 텍스트만 가져옴
            if len(row.cells) >= 2:
                cells = [row.cells[0].text, row.cells[1].text]
                rows.append(cells)
            else:
                rows.append([cell.text for cell in row.cells])
                # "방송일지" 단어를 확인하여 파일을 나눔
                if any("방송일지" in cell.text for cell in row.cells):
                    if current_table:
                        tables.append(current_table)
                    current_table = []
        current_table.append(rows)
    tables.append(current_table)  # 마지막 테이블 추가
    return tables

def write_tables_to_txt(tables, file_prefix):
    file_counter = 1
    for table in tables:
        for rows in table:
            for row in rows:
                # "방송일지"라는 단어가 포함된 행의 텍스트를 확인하고 파일명 추출
                if any("방송일지" in cell for cell in row):
                    for cell in row:
                        if "방송일지" in cell:
                            # 파일명으로 사용할 문자열 추출
                            date_string = cell.split("방송일지")[1].strip()
                            txt_file = f'C:/Users/user/Desktop/list/{date_string}.txt'
                            with open(txt_file, 'w', encoding='utf-8') as file:
                                for rows in table:
                                    file.write("\n")
                                    for row in rows:
                                        # 행에 셀이 있는 경우에는 탭으로 구분하여 출력하고,
                                        # 행에 셀이 없는 경우에는 텍스트만 출력
                                        if len(row) == 2:
                                            row_text = '\t'.join(row)
                                        else:
                                            row_text = '\t'.join(row)
                                        file.write(row_text + '\n')
                                    file.write('\n')
                    break
        file_counter += 1

# .docx 파일 경로
docx_file = input()

# 표를 읽어옴
table_data = read_tables_from_docx(docx_file)

# 파일 분할하여 저장
file_prefix = "방송일지"
write_tables_to_txt(table_data, file_prefix)

print("표가 성공적으로 출력되었습니다.")
