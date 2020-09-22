# 컬러이미지의 레드값 제거
import numpy as np
import cv2 as cv


img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

print('type(img) = ', type(img))
print('img.shape, img.dtype =', img.shape, img.dtype)

img[:,:,1] = 0
cv.imshow('img', img)
key = cv.waitKey()
