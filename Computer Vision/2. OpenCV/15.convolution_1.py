# Blur gray image

import cv2 as cv
import numpy as np


def filter_gray(img, kernel):

    kh, kw = kernel.shape[0:2]
    kh2, kw2 = kh//2, kw//2
    # kernel의 중심픽셀을 기준으로 크기를 구함    return filtered.sum()

    tmp_shape = list(img.shape)
    tmp_shape[0] += kh2 * 2
    tmp_shape[1] += kw2 * 2
    # 약간 더 큰 이미지 필터 생성


    tmp = np.zeros(tmp_shape, img.dtype)
    cv.imshow('tmp', tmp)
    np.copyto(tmp[kh2:kh2+img.shape[0], kw2:kw2+img.shape[1]], img)
    # original에 tmp이미지를 합성하여 zero padding 적용

    dst = np.zeros(img.shape, img.dtype)

    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            dst[i, j] = (tmp[i:i+kh, j:j+kw] * kernel).sum()
            # 각 픽셀마다 대응해서 convolution

    return dst

img = cv.imread('filter_blur.jpg', cv.IMREAD_GRAYSCALE)
ksize = 9 # kernel size
kernel = np.full((ksize, ksize), 1./(ksize * ksize))
# kernel 을 채워줌   blur처리를 위해선 커널값을 평균을 내준다(1/(ksize, ksize)
img_filtered = filter_gray(img, kernel)



cv.imshow('original',img)
cv.imshow('filter', img_filtered)
cv.waitKey()