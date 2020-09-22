# wrong edge detection

import cv2 as cv
import numpy as np

kernel_diag0 = np.array([[-1,  0,  0],
                         [ 0,  1,  0],
                         [ 0,  0,  0]])

kernel_diag1 = np.array([[ 0,  0, -1],
                         [ 0,  1,  0],
                         [ 0,  0,  0]])

kernel_all_in_one0 = np.array([[-1,  0, -1],
                               [ 0,  2,  0],
                               [ 0,  0,  0]])

kernel_all_in_one1 = np.array([[ 0, -1,  0],
                               [-1,  4, -1],
                               [ 0, -1,  0]])

img = np.zeros((400,400), np.uint8)

j0, j1 = 200, 203
d = j1 - j0
for j in range(j0, j1):
	img[:,j] = int(255*(j-j0)/d)

img[:, j1:]	= 255

dst_diag0 = cv.filter2D(img, cv.CV_32F, kernel_diag0)
dst_diag1 = cv.filter2D(img, cv.CV_32F, kernel_diag1)
dst_diag = cv.magnitude(dst_diag0, dst_diag1)

dst_all_in_one0 = cv.filter2D(img, cv.CV_32F, kernel_all_in_one0)
dst_all_in_one1 = cv.filter2D(img, cv.CV_32F, kernel_all_in_one1)

cv.imshow('img', img)
cv.imshow('dst_diag', np.abs(dst_diag).astype(np.uint8))
cv.imshow('dst_all_in_one0', np.abs(dst_all_in_one0).astype(np.uint8))
cv.imshow('dst_all_in_one1', np.abs(dst_all_in_one1).astype(np.uint8))
cv.waitKey()