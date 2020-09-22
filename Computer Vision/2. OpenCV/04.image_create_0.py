import cv2 as cv
import numpy as np

# 검정색 이미지 생성
img = np.zeros((400, 640, 3), dtype=np.uint8)
cv.imshow('img', img)
cv.waitKey()
