import cv2 as cv
import numpy as np

blue = [255,0,0]
green = [0,255,0]
red = [0,0,255]
img = np.zeros((300,400,3), dtype=np.uint8)
img[:100,] = blue
img[100:200,] = green
img[200:,] = red
cv.imshow('img',img)
cv.waitKey()

cv.imshow('img', img)
cv.waitKey()