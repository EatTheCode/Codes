# 원본 이미지 읽기
import cv2 as cv

print(cv.__version__)

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

print('type(img) = ', type(img))
print('img.shape, img.dtype =', img.shape, img.dtype)
# RGB이기 때문에 dtype은 3