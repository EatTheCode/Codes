# 비디오 재생

import cv2 as cv

capture = cv.VideoCapture('capture.avi')
fps = capture.get(cv.CAP_PROP_FPS)
dt = int(1000./fps)
# 프레임을 맞춰주기 위함

while True:
    ret, frame = capture.read()
    if ret:
        cv.imshow('frame', frame)
    else:
        break
    if cv.waitKey(dt) == 27:break

capture.release()