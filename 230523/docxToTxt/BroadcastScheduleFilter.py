import codecs
import os
from common import strip_quotes

class TimetableConverter:
    def __init__(self):
        self.timetable = ""
        self.last_hour = 0

    def convert_time(self, time_str):
        if len(time_str) == 5:
            hour = int(time_str[:2])
            minute = int(time_str[3:])
        else:
            hour = self.last_hour
            minute = int(time_str.strip()) if time_str.strip() else 0
        return f"{hour:02d}:{minute:02d}"

    def simplify_time(self, time_str):
        if len(time_str) == 3:
            if time_str[0] == time_str[1]:
                return time_str[1:]
            if time_str[1] == time_str[2]:
                return time_str[:2]
        return time_str

    def load_timetable(self, file_path):
        file_path = strip_quotes(file_path)
        with codecs.open(file_path, 'r', encoding='utf-8') as file:
            self.timetable = file.read()

    def convert_timetable(self):
        new_timetable = ""
        lines = self.timetable.split("\n")
        for line in lines:
            parts = line.split("\t")
            if len(parts) >= 2:
                start_time = parts[0]
                new_start_time = self.convert_time(start_time)
                self.last_hour = int(new_start_time[:2])
                simplified_time = self.simplify_time(new_start_time[3:])
                new_timetable += f"{new_start_time[:3]}{simplified_time}\t{parts[1]}\n"
        return new_timetable

if __name__ == "__main__":
    converter = TimetableConverter()
    file_path = strip_quotes(input("Enter the file path: "))
    
    converter.load_timetable(file_path)
    new_timetable = converter.convert_timetable()

    file_name, file_extension = os.path.splitext(file_path)
    new_file_path = f"{file_name}_new{file_extension}"

    with codecs.open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(new_timetable)

    print(f"Converted timetable saved to: {new_file_path}")
