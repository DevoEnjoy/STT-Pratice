# xml_generator.py
import os
from xml.etree.ElementTree import Element, dump, indent
class Data_generator:
    label = Element("label")
    starttime = Element("starttime")
    endtime = Element("endtime")
    word = Element("word")
    stt_word = Element("stt_word")

    def __init__(self, starttime, endtime, word):
        self.starttime.text = starttime
        self.endtime.text = endtime
        self.word.text = word
        self.stt_word.text = " "
    
    def setStt_word(self, stt_word):
        self.stt_word.text = stt_word

    def label_generate(self):
        self.label.append(self.starttime)
        self.label.append(self.endtime)
        self.label.append(self.word)
        self.label.append(self.stt_word)

class Xml_generator:
    annotation = Element("annotation")
    folder = Element("folder")
    filename = Element("filename")
    filename_origin = Element("filename_origin")
    starttime_origin = Element("starttime_origin")
    endtime_origin = Element("endtime_origin")
    text = Element("text")
    duration = Element("duration")

    def __init__(self, folderPath, filename, filename_origin, starttime_origin, endtime_origin, text, duration, datas):
        self.folder.text = folderPath
        self.filename.text = filename
        self.filename_origin.text = filename_origin
        self.starttime_origin.text = starttime_origin
        self.endtime_origin.text = endtime_origin
        self.text.text = text
        self.duration.text = duration
        self.append_header()
        

    def append_labels(self, datas):
        for data in datas:
            data.label_generate()
            self.annotation.append(data.label)

    def append_header(self):
        self.annotation.append("<?xml version='1.0' encoding='utf-8'?>")
        self.annotation.append(self.folder)
        self.annotation.append(self.filename)
        self.annotation.append(self.filename_origin)
        self.annotation.append(self.endtime_origin)
        self.annotation.append(self.starttime_origin)
        self.annotation.append(self.text)
        self.annotation.append(self.duration)

    # def setFolderPath(self, folderPath):
    #     self.folder.text = folderPath
    
    # def setFilename(self, filename):
    #     self.filename.text = filename
    


# annotation = Element("annotation")
# folder = Element("folder")
# folder.text = "/data/nfs/wyd/script_exist_data/"
# E20200904_00001_audio
file_path = "D:/practicePlace/workbench/label/"
file_list = os.listdir(file_path)

for i in range(len(file_list)): #label.txt 파일 하나의 정보
    readFileName = file_list[i]
    readFileNameWithoutExt = readFileName.rstrip('.txt')
    # year = readFileName[1:5]
    # month = readFileName[5:9]
    numbering = readFileName[10:15]
    readFile = open(file_path + "/" + readFileName, 'r', encoding='UTF8')
    # readlines = readFile.readlines()
    # readlineList = list()
    lineData = []   # 한 줄을 탭 단위로 나눠서 리스트 형태로 리스트에 담음
    textList = list()   # text 태그에 담을, 문장 전체 내용
    j = 0
    # for line in readlines: # 파일 내용 한 줄씩 가져오기
    while True:
        line = readFile.readline()
        print("=" * 10)
        print("line")
        print(j)
        print(line)
        # print(line.rstrip('\n'))
        if not line: break
        # readlineList.append(line)
        # print(line.split('\t'))
        lineData.append(line.rstrip('\n').split('\t'))
        if len(lineData[j]) > 0:
            if 'text' in lineData[j][2]:
                text = lineData.pop(j)
                textList.append(text)
        j = j + 1
    # totalLength = lineData.pop(largest)
    datas = list()
    j2 = 0
    # print(textList[i])
    for data in lineData:
        if len(data) == 3:
            realData = Data_generator(data[0], data[1], data[2])
            realData.label_generate()
            datas.append(realData)
    playLength = float(textList[i][1]) - float(textList[i][0])
    xml = Xml_generator(file_path, readFileNameWithoutExt, readFileName
                        , textList[i][0], textList[i][1], textList[i][2]
                        , playLength, datas)
    xml.append_labels(datas)
    indent(xml.annotation)
    dump(xml.annotation)




    # readFile = open("D:/result/" year "/" month "/")

##
# data1 = Data_generator("0.0", "0.24", "오늘")
# data1.label_generate()

# datas = list()
# datas.append(data1)
# datas.append(data1)
# datas.append(data1)
# xml = Xml_generator("D:/source/new/04", "20160214_보도_2_", "20160214_보도_2_.mp4"
#                     , "400.375461", "404.012363", "오늘 같은 기쁜 날에 한 번 나도 나서서"
#                     , "3.6369020000000205", datas)

# xml.append_labels(datas)
# indent(xml.annotation)
# dump(xml.annotation)