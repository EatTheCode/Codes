# 그림을 채널별로 분리

import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

b, g, r = cv.split(img)


# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
# cv.waitKey()
# 값을 많이 소유할 수록 밝게 나온다