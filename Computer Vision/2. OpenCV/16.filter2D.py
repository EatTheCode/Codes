import cv2 as cv
import numpy as np

img = cv.imread('filter_blur.jpg')
kernel = np.full((9,9), 1./(9*9)) # 9 * 9
# blur처리         각각의 숫자는 필터의 방향성을 나타낸다

img_filtered = cv.filter2D(img, -1, kernel)
#                              -1 = 원본과 똑같은 depth


cv.imshow('filter', img_filtered)
cv.waitKey()
print(img.shape, img.dtype)
print(img_filtered.shape, img_filtered.dtype)