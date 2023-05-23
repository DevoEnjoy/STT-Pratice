import os


class TextFileProcessor:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def process_file(self):
        base_path = os.path.dirname(self.input_filename)
        file_name = os.path.basename(self.input_filename)
        output_filename = os.path.join(base_path, f"{os.path.splitext(file_name)[0]}_fixed.txt")

        with open(self.input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        filtered_lines = [line.strip() for line in lines if not line.strip() or any(char.isdigit() for char in line)]

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(filtered_lines))


# 사용 예시
input_filename = input()

processor = TextFileProcessor(input_filename)
processor.process_file()
