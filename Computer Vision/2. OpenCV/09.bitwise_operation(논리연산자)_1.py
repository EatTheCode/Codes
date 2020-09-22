# or xor not
import cv2 as cv
import numpy as np


img1 = np.zeros((300, 300), np.uint8)
img2 = np.zeros((300, 300), np.uint8)
mask = np.zeros((300, 300), np.uint8)

cv.circle(img1, (150, 150), 100, 255, -1)
cv.rectangle(img2, (0, 0), (150, 300), 255, -1)
cv.rectangle(mask, (0, 0), (300, 150), 255, -1)


img1_or_img2 = cv.bitwise_or(img1, img2)
# or 연산
img1_or_img2_mask = cv.bitwise_or(img1, img2, mask = mask)
# or mask 연산
img1_not_img2 = cv.bitwise_not(img1, img2)
# not 연산
img1_not_img2_mask = cv.bitwise_not(img1, img2, mask = mask)
# not mask 연산
img1_xor_img2 = cv.bitwise_xor(img1, img2)
# xor 연산
img1_xor_img2_mask = cv.bitwise_xor(img1, img2, mask = mask)
# xor mask 연산

cv.imshow('img1_or_img2', img1_or_img2)
cv.imshow('img1_not_img2', img1_not_img2)
cv.imshow('img1_xor_img2', img1_xor_img2)
cv.imshow('img1_or_img2_mask', img1_or_img2_mask)
cv.imshow('img1_not_img2_mask', img1_not_img2_mask)
cv.imshow('img1_xor_img2_mask', img1_xor_img2_mask)

cv.waitKey()