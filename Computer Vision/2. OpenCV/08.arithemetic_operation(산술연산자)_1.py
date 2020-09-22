import cv2 as cv
import numpy as np

img1 = cv.imread('add1.jpg', cv.IMREAD_UNCHANGED)
img2 = cv.imread('add2.jpg', cv.IMREAD_UNCHANGED)

print('type(img1) = ', type(img1))
print('img1.shape, img1.dtype =', img1.shape, img1.dtype)

print('type(img2) = ', type(img2))
print('img2.shape, img2.dtype =', img2.shape, img2.dtype)

ad = cv.add(img1, img2)

cv.imshow('ad', ad)
cv.waitKey()