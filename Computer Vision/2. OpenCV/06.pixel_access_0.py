import numpy as np
import cv2 as cv

img = np.zeros((480, 640, 3), dtype=np.uint8)

img[240, 320] = (0,255,0)
#리스트나 튜플로 넣어주는게 가능함
img[244, 322] = [0, 255, 0]
