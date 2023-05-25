# secondProcess.py
"""
TextFileProcessor 클래스는 input_filename과 suffix라는 두 개의 매개변수를 받아 객체를 초기화합니다. input_filename은 입력 파일의 경로를 나타내고, suffix는 출력 파일의 이름에 추가될 접미사입니다. suffix 매개변수는 기본값으로 "second"를 가지며, 따로 지정하지 않으면 "second"가 사용됩니다.

process_file() 메서드는 입력 파일을 처리하고, 결과를 출력 파일에 저장합니다. 처리 과정은 다음과 같습니다:

self.input_filename에서 파일의 디렉토리 경로와 파일 이름을 추출합니다.
출력 파일의 이름을 생성하기 위해 기존 파일 이름에서 밑줄(_)로 구분된 첫 번째 부분을 추출하고, 이에 self.suffix를 추가합니다. 그리고 확장자 .txt를 붙여 완전한 출력 파일 이름을 생성합니다.
입력 파일을 읽어들여 각 줄을 리스트로 저장합니다.
각 줄을 순회하면서 공백을 제거한 후, 문자열에 숫자가 포함되어 있는지 확인합니다.
숫자가 포함된 줄에서 추가적인 탭 문자를 제거한 후, processed_lines 리스트에 추가합니다.
최종 처리된 줄들을 문자열로 변환하고, 출력 파일에 씁니다.
run(file_path, suffix) 메서드는 정적 메서드(static method)로 정의되어 있으며, file_path와 suffix 매개변수를 받습니다. file_path는 따옴표로 둘러싸인 파일 경로 문자열을 나타내는 것으로 추측됩니다. 이 메서드는 strip_quotes() 함수를 사용하여 file_path에서 따옴표를 제거하고, TextFileProcessor 객체를 생성하여 파일 처리를 수행합니다.

코드의 가장 아래 부분에서 __name__ 변수가 "__main__"과 같은지 확인하여 현재 모듈이 직접 실행되었는지 여부를 판단합니다. "__main__"과 같다면 TextFileProcessor.run()을 호출하여 프로그램을 실행합니다.
"""
import os
from common import strip_quotes
from common import remove_extra_tabs as strip_tab
""" 결과 예시
방송일지                                                              2020년 10월 1일
09:00	※ 방송시작 ( 위성파 - 수신양호 )
05	오늘의 순서
"""
class TextFileProcessor:
    def __init__(self, input_filename, suffix="second"):
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
                processed_line = stripped_line.replace('  ', ' ').replace('\t\t', '\t').replace('\t\t', '\t').replace('보\t도\t시\t작', '보도시작').replace('보\t도\t종\t료', '보도종료').replace('음\t악', '음악')
                processed_lines.append(processed_line)

        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(processed_lines))

def run(file_path, suffix="second"):
    input_filename = strip_quotes(file_path)
    processor = TextFileProcessor(input_filename, suffix)
    processor.process_file()


if __name__ == "__main__":
    filename = input()
    run(filename)