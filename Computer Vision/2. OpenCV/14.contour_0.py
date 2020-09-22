import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

cv.circle(img, (200, 150), 80, (255, 255, 0), -1)
cv.circle(img, (500, 150), 50, (255, 0, 0), -1)
cv.rectangle(img, (300, 300), (500,400), (0, 255,255), -1)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 회색이미지로 변환
_, img_thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
# threshold 함수 임계값 지정 150보다 큰값은 255로 지정, 이미지를 이진함수로 변환
contours, _ = cv.findContours(img_thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# 물체의 외곽선 추출 = contour                                  # 근사치 추출(APPORX_SIMPLE)의 경우 점으로 출력

print('contours')
for c in contours:
    print(c.shape, c.dtype, cv.contourArea(c)) # type = numpy
                                # contour의 영역 계산

for i in range(contours[0].shape[0]): # 영역을 따라 마킹
    cv.circle(img, (contours[0][i][0][0], contours[0][i][0][1]), 3, (0, 255, 0), -1)
                        # x 좌표             y좌표
             # contours[0] = original shape

cv.drawContours(img, contours, 1, (0, 0, 255), 3)
# contour값을 자동으로 찾아주는 함수 첫번째(-1로 입력시 모든 정의된 도형 contour)


cv.imshow('img', img)
cv.imshow('img_gray', img_gray)
cv.imshow('img_thresh', img_thresh)
cv.waitKey()
