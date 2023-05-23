import os
from common import strip_quotes
from common import remove_extra_tabs as strip_tab

class TextFileProcessor:
    def __init__(self, input_filename, suffix):
        self.input_filename = input_filename
        self.suffix = suffix

    def process_file(self):
        base_path = os.path.dirname(self.input_filename)
        file_name = os.path.basename(self.input_filename)
        output_filename = os.path.join(base_path, f"{os.path.splitext(file_name)[0].split('_')[0]}_{self.suffix}.txt")

        with open(self.input_filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        processed_lines = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line and any(char.isdigit() for char in stripped_line):
                processed_line = strip_tab(stripped_line)
                processed_lines.append(processed_line)

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(processed_lines))

    def run(file_path, suffix):
        input_filename = strip_quotes(file_path)
        processor = TextFileProcessor(input_filename, suffix)
        processor.process_file()


if __name__ == "__main__":
    TextFileProcessor.run()
