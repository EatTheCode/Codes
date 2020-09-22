# fps를 측정해서 화면에 출력하기

import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
count = 0
fps = 0
t0 = cv.getTickCount()
# 시간의 흐름을 기록

while True:
    ret, frame = capture.read()
    cv.putText(frame, str(fps), (10, 60), cv.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 3)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27: break

    count += 1
    if count == 10:
        t = cv.getTickCount()
        time = (t - t0) / cv.getTickFrequency()
        # 열장의 프레임이 얻어지는데 걸리는 시간 측정
        # fps = frame / time
        fps = int(np.round(count / time))
        count = 0
        t0 = t

capture.release()
cv.getTickFrequency()
# 주파수 = 카운트 / 걸린시간
# 걸린시간 = 카운트 / 주파수

# 특정 시간동안 몇장의 이미지가 얻어지는지 측정

