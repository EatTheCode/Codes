import cv2 as cv


H = cv.imread('cat_h.png', cv.IMREAD_UNCHANGED)
S = cv.imread('cat_s.png', cv.IMREAD_UNCHANGED)
V = cv.imread('cat_v.png', cv.IMREAD_UNCHANGED)

# 하나의 HSV이미지로 만들기

HSV = cv.merge((H,S,V))
bgr = cv.cvtColor(HSV, cv.COLOR_HSV2BGR)

cv.imshow('hsv', HSV)
cv.imshow('bgr', bgr)
cv.waitKey()