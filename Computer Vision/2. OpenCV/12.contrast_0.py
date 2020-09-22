import cv2 as cv
# 이미지를 밝게 만들기
# 이미지 픽셀값을 늘려줌

img0 = cv.imread('cat.jpg')
img1 = cv.addWeighted(img0, 1.5, img0, 0, 0)


cv.imshow('img0', img0)
cv.imshow('img1', img1)
cv.waitKey()