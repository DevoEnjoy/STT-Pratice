# docxToTxt.py
def convert_time(time_str, last_hour):
    if len(time_str) == 5:
        hour = int(time_str[:2])
        minute = int(time_str[3:])
    else:
        hour = last_hour
        minute = int(time_str)
    return f"{hour:02d}:{minute:02d}"

def simplify_time(time_str):
    if len(time_str) == 3:
        if time_str[0] == time_str[1]:
            return time_str[1:]
        if time_str[1] == time_str[2]:
            return time_str[:2]
    return time_str

# 기존의 방송시간표
timetable = """09:00\t※ 방송시작 ( 위성파 - 수신양호 )
05\t오늘의 순서
12\t김정은 명언 ( 우리 나라는 김일성동지와 김정일동지를 높이 모시고 받들어나가는 영원한 태양의 나라이다… )
13\t음악 ( 조국찬가 )
18\t김정은, 당중앙위원회 제7기 제18차 정치국회의 진행
21\t음악 ( 높이 날려라 우리의 당기 )
26\t음악 ( 우리에겐 위대한 당이 있네 )
30\t련속편집물 ( 태양의 모습으로 길이 빛날 불멸의 대기념비들 )
10:13\t음악 ( 사회주의 전진가 )
188\t련속참관기 ( 위인칭송의 고귀한 재보, 35 )
23\t특집 ( 민족의 시조를 찾아주시여 )"""

# 새로운 방송시간표 작성
new_timetable = ""
last_hour = 0
lines = timetable.split("\n")
for line in lines:
    parts = line.split("\t")
    start_time = parts[0]
    new_start_time = convert_time(start_time, last_hour)
    last_hour = int(new_start_time[:2])
    simplified_time = simplify_time(new_start_time[3:])
    new_timetable += f"{new_start_time[:3]}{simplified_time}\t{parts[1]}\n"

# 결과 출력
print(new_timetable)
