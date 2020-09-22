import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('img', img)
key = cv.waitKey(3000)
print(key)
# 키보드 입력이 들어올때 까지 기다림 단위는 밀리 세컨드
