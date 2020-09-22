# 컬러이미지를 읽어서 흑백으로 저장
import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('img', img)
cv.waitKey()
cv.imwrite('cat-gray.jpg', img)
