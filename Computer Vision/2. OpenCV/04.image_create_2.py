import cv2 as cv
import numpy as np

h = 480; w = 640
img = np.zeros((h,w,3), dtype=np.uint8)


img[h*1//3:h*2//3, w*1//3:w*2//3] = (0,255,0)

cv.imshow('img', img)
cv.waitKey()

img[240, 320] = (0, 255, 0)
# 아래와 같은 의미
img[240, 320, 0] = 0
img[240, 320, 1] = 255
img[240, 320, 2] = 0