import cv2 as cv
import numpy as np

# 이미지를 표현하는 방식
# HSV 또한 rgb처럼 3차원 공간으로 표현 가능 saturation, 채도 밝기


bgr = cv.imread('cat.jpg')
HSV = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
H, S, V = cv.split(HSV)

cv.imshow('bgr', bgr)
cv.imshow('H', H)
cv.imshow('S', S)
cv.imshow('V', V)
cv.waitKey()

cv.imwrite('cat_h.png', H)
cv.imwrite('cat_s.png', S)
cv.imwrite('cat_v.png', V)