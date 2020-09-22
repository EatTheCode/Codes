import cv2 as cv
import numpy as np
# bit단위 연산 (1, 0 으로 이루어져 나누어진 단위가 계산되는 형태)

img1 = np.zeros((300, 300), np.uint8)
img2 = np.zeros((300, 300), np.uint8)
mask = np.zeros((300, 300), np.uint8)

cv.circle(img1, (150, 150), 100, 255, -1)
#                 사이즈     반지름 색깔   선두께
cv.rectangle(img2, (0, 0), (150, 300), 255, -1)
#                  x좌표     y좌표
cv.rectangle(mask, (0, 0), (300, 150), 255, -1)

img1_and_img2 = cv.bitwise_and(img1, img2)
# and 연산 실행
img1_or_img2 = cv.bitwise_or(img1, img2)
# or 연산
img1_and_img2_mask = cv.bitwise_and(img1, img2, mask=mask)
# mask 그림의 흰색부분에 대해서만 연산함
dst_img = np.full((300, 300), 127, dtype = np.uint8)
# 회색이미지 생성(모든값을 10으로 초기화)
cv.bitwise_and(img1, img2, dst=dst_img, mask = mask)
#dst=결과를 반환받거나 실행할 장소


cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('mask', mask)
cv.imshow('img1_and_img2', img1_and_img2)
cv.imshow('img1_or_img2', img1_or_img2)
cv.imshow('img1_and_img2_mask', img1_and_img2_mask)
cv.imshow('dst', dst_img)
# 마스크가 지정하지 않은 영역은 and 연산 적용x
# 공통된 영역만 남겨놓는다(and 연산)

cv.waitKey()
