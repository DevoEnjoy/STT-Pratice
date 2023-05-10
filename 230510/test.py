# test.py
import cv2

print("타임랩스 생성 시작")

# 동영상 읽어오기(앞에서 쓴 코드와 동일)
cap = cv2.VideoCapture("mov/mov01.avi")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# hog 모델 - 사람 인식(앞에서 쓴 코드와 동일)
hog = cv2.HOGDescriptor()  # 객체
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 모델지정
hogParams = {
    "winStride": (8, 8),
    "padding": (32, 32),
    "scale": 1.05,
    "hitThreshold": 0,
    "finalThreshold": 5,
}  # 파라미터 설정


# 타임랩스 작성
movie_name = "timelapse2.avi"
fourcc = cv2.VideoWriter_fourcc(*"XVID")  #'X', 'V', 'I', 'D'로 써도 됨
video = cv2.VideoWriter(movie_name, fourcc, 30, (width, height))

num = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 10으로 나누어 떨어지는 경우만(41개 프레임만)
        if num % 10 == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            human, r = hog.detectMultiScale(gray, **hogParams)
            if len(human) > 0:
                for x, y, w, h in human:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 3)
            video.write(frame)

    else:
        break
    num += 1

# 타임랩스 종료 및 발행
video.release()
cap.release()
cv2.destroyAllWindows()
print("타임랩스 생성 완료")
