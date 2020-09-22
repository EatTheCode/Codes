import cv2 as cv
import numpy as np

h = 480; w = 640
img = np.zeros((h,w,3), dtype=np.uint8)

img[h*0//3:h*1//3, :] = (255,0,0)
img[h*1//3:h*2//3, :] = (0,255,0)
img[h*2//3:h*3//3, :] = (0,0,255)
cv.imshow('img', img)
cv.waitKey()