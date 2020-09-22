import cv2 as cv
import numpy as np

img = cv.imread('edge_test.jpg', cv.IMREAD_GRAYSCALE)

kernel1 = np.array([[-1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0]])
kernel2 = np.array([[0, 0, -1],
                    [0, 1, 0],
                    [0, 0, 0]])

dst1 = cv.filter2D(img, cv.CV_32F, kernel1)
dst2 = cv.filter2D(img, cv.CV_32F, kernel2)
# 변화가 있는 부분을 edge로 검출

cv.imshow('img', img)
cv.imshow('dst1', np.abs(dst1).astype(np.uint8))
cv.imshow('dst2', np.abs(dst2).astype(np.uint8))
cv.waitKey()