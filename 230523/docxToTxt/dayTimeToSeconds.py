from common import *


def calculate_cumulative_duration(start_times):
    cumulative_seconds = [0]
    for i in range(1, len(start_times)):
        start_hour, start_minute = map(int, start_times[i].split(':'))
        prev_hour, prev_minute = map(int, start_times[i - 1].split(':'))

        start_seconds = start_hour * 3600 + start_minute * 60
        prev_seconds = prev_hour * 3600 + prev_minute * 60

        cumulative_duration = cumulative_seconds[i - 1] + (start_seconds - prev_seconds)
        cumulative_seconds.append(cumulative_duration)

    return cumulative_seconds


def parse_broadcast_schedule(file_path):
    file_path = strip_quotes(file_path)
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()
    broadcast_infos = []
    start_times = []
    for line in lines:
        start_time, broadcast_info = line.split('\t')
        start_times.append(start_time)
        broadcast_infos.append(broadcast_info)
    cumulative_durations = calculate_cumulative_duration(start_times)

    # 파일명에 "suffix"를 추가하여 새로운 파일명 생성
    output_file_path = changeSufficWithoutUnderbar(file_path, "")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for i in range(len(cumulative_durations)):
            if i+1 == len(cumulative_durations):
                output_file.write(f"{cumulative_durations[i]}\t{broadcast_infos[i].strip()}\n")
            else:
                output_file.write(f"{cumulative_durations[i+1]}\t{broadcast_infos[i].strip()}\n")

    print(f"결과가 {output_file_path}에 저장되었습니다.\n")
    return output_file_path

def parse_broadcast_schedule_timeToTime(file_path):
    file_path = strip_quotes(file_path)
    with open(file_path, encoding='utf-8') as file:
        lines = file.readlines()
    broadcast_infos = []
    start_times = []
    last_times = []
    for line in lines:
        splitline = line.split('\t')
        start_time, last_time, broadcast_info = splitline[0], splitline[1], splitline[2]
        start_times.append(start_time)
        last_times.append(last_time)
        broadcast_infos.append(broadcast_info)
    cumulative_durations_start = calculate_cumulative_duration(start_times)
    cumulative_durations_last = calculate_cumulative_duration(last_times)


    # 파일명에 "_new"를 추가하여 새로운 파일명 생성
    output_file_path = changeSufficWithoutUnderbar(file_path, "")

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for i in range(len(cumulative_durations_start)):
            if i+1 == len(cumulative_durations_start):
                output_file.write(f"{cumulative_durations_start[i]}\t{cumulative_durations_last[i]+cumulative_durations_start[0]}\t{broadcast_infos[i].strip()}\n")
            else:
                output_file.write(f"{cumulative_durations_start[i+1]}\t{cumulative_durations_last[i+1]+cumulative_durations_start[0]}\t{broadcast_infos[i].strip()}\n")

    print(f"결과가 {output_file_path}에 저장되었습니다.\n")
    return output_file_path


def run(file_path):
    return parse_broadcast_schedule(file_path)

def run2(file_path):
    return parse_broadcast_schedule_timeToTime(file_path)

if __name__ == "__main__":
    # 텍스트 파일 경로 입력 받기
    file_path = input("텍스트 파일 경로를 입력하세요: ")
    parse_broadcast_schedule(file_path)
