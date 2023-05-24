# fourthProcess.py
from common import *
""" 출력 예시
09:00	09:05	※ 방송시작 ( 위성파 - 수신양호 )
09:05	09:12	오늘의 순서
...
22:58	23:03	음악 ( 지새지 말아다오 평양의 밤아 )
23:03	23:03	래일의 순서
"""
class fourthProcess:

    def __init__(self) -> None:
        self.times = []
        self.contents = []
        pass

    def split_line_info(self, filename):
        
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    line_info = line.split('\t')
                    time = line_info[0]
                    content = line_info[1]
                    self.times.append(time)
                    self.contents.append(content)

def run(filename, suffix="fourth"):
    this = fourthProcess()
    filename = strip_quotes(filename)
    this.split_line_info(filename)
    origin_start_time = this.times[0]
    i = 1
    line = []
    #line.append(origin_start_time + '\t' + this.times[0] + '\t' + this.contents[0])
    for i in range(len(this.contents)):
        if i+1==len(this.contents):
            line.append(this.times[i] + '\t' + this.times[i] + '\t' + this.contents[i])
        else:
            line.append(this.times[i] + '\t' + this.times[i+1] + '\t' + this.contents[i])
            
    # filename = filename.split('_')[0] + "_" + suffix + '.txt'
    filename = changeSufficWithUnderbar(filename, suffix)
    write_to_file(filename, line)
    return filename

if __name__ == "__main__":
    # 사용 예시
    filename = input()  # 읽어올 파일명을 지정합니다
    result = run(filename)  # 메서드를 호출
    print(result)  # 결과 리스트를 출력합니다
