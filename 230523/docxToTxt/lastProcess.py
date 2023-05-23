# lastProcess.py
class lastProcess:

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

    def run(self, filename):
        self.split_line_info(filename)
        origin_start_time = self.times[0]
        self.times.pop(0)
        i = 0
        result = []
        result.append(origin_start_time + '\t' + self.times[0] + '\t' + self.contents[0])
        for i in range(len(self.contents)):
            if i+1<len(self.contents):
                result.append(self.times[i] + '\t' + self.times[i+1] + '\t' + self.contents[i])
            else:
                result.append(self.times[i] + '\t' + self.times[i] + '\t' + self.contents[i])
        filename = filename.split('_')[0] + '.txt'
        write_to_file(filename, result)
        return filename



def write_to_file(filename, values):
    with open(filename, 'w') as file:
        for value in values:
            file.write(value + '\n')

if __name__ == "__main__":
    # 사용 예시
    filename = input()  # 읽어올 파일명을 지정합니다
    result = lastProcess.run(filename)  # 메서드를 호출
    print(result)  # 결과 리스트를 출력합니다
