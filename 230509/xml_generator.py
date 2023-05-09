# xml_generator.py
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
data1 = Data_generator("0.0", "0.24", "오늘")
data1.label_generate()

datas = list()
datas.append(data1)
datas.append(data1)
datas.append(data1)
xml = Xml_generator("/data/nfs/wyd/script_exist_data/", "20160214_보도_2_", "20160214_보도_2_.mp4", "400.375461", "404.012363", "오늘 같은 기쁜 날에 한 번 나도 나서서", "3.6369020000000205", datas)

xml.append_labels(datas)
indent(xml.annotation)
dump(xml.annotation)