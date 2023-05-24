# common.py
import os
def strip_quotes(text):
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    return text

def remove_extra_tabs(text):
    lines = text.split('\n')
    processed_lines = []

    for line in lines:
        parts = line.split('\t')
        if len(parts) > 1:
            processed_line = ''
            for part in parts:
                if part == parts[0]:
                    continue
                processed_line = processed_line + part.strip('\t')
            processed_lines.append(parts[0] + '\t' + processed_line)
        else:
            processed_lines.append(line)

    processed_text = '\n'.join(processed_lines)
    return processed_text

def delete_file(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"파일 '{file_name}'이(가) 삭제되었습니다.")
    else:
        print(f"파일 '{file_name}'을(를) 찾을 수 없습니다.")

if __name__ == "__main__":
    folder_path = '/경로/폴더'  # 실제 폴더 경로로 대체해야 합니다.
    file_name = 'example.txt'  # 실제 파일명으로 대체해야 합니다.
    delete_file(folder_path, file_name)

def get_txt_files_in_folder(folder_path):
    txt_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            txt_files.append(file_name)
    return txt_files

if __name__ == "__main__":
    folder_path = '/path/to/your/folder'  # 실제 폴더 경로로 변경해주세요
    txt_files_list = get_txt_files_in_folder(folder_path)
    print(txt_files_list)

def write_to_file(filename, values):
    with open(filename, 'w', encoding="UTF-8") as file:
        for value in values:
            file.write(value + '\n')

def changeSufficWithUnderbar(filename, suffix):
    return filename.split('_')[0] + "_" + suffix + '.txt'

def changeSufficWithoutUnderbar(filename, suffix):
    return filename.split('_')[0] + suffix + '.txt'