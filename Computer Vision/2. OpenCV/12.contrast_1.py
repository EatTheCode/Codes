# 밝기는 유지하되 대비만 증가

import cv2 as cv
import numpy as np

img0 = cv.imread('cat.jpg')
mean = np.zeros(img0.shape, np.uint8)
# rgb 채널별 평균색상을 구함
mean[:, :] = np.mean(img0, (0, 1))
#                        (0, 1)  이미지의 넓이와 길이 방향으로 컬러를 스캔

scale = 1.5


#x 와 y축의 모든 범위 = 모든 픽셀

# y = scale * (img0 - mean) + mean
# y = scale * img0 - scale * mean + mean
# y = img0 * scale + mean * (1 - scale) + 0 = img1
# 새로운 이미지 생성
img1 = cv.addWeighted(img0,scale,mean,1-scale,0)


cv.imshow('img1', img0)
cv.imshow('mean', mean)
cv.imshow('img1', img1)
cv.waitKey()