import cv2 as cv
import numpy as np

h = 480; w = 640
img = np.zeros((h,w,3), dtype=np.uint8)

cv.imshow('img', img)
cv.waitKey()
cv.imwrite('img.png', img)