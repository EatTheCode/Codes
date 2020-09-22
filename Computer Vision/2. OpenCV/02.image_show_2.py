# ESC 키가 눌러질때까지 그림을 보여주기

# ESC의 키값을 탐색 후 루프를 돌면서 일정한 시간 간격으로 키값을 체크해서 ESC가 눌렸으면 종료

import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('img', img)

while True:

    key = cv.waitKey(30)
    if key == 27: break
print(key)