import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)


#직선 그리기
cv.line(img, (20, 20), (640, 640), (0, 255, 0), 3)
#       위치 첫번째좌표 두번째좌표   선의 색깔  굵기

# 사각형 그리기
cv.rectangle(img, (100,100), (400, 400), (0,0,255), 3)

# 채워진 사각형
cv.rectangle(img, (500, 100), (600, 200), (255,0,0), -1)

# 원그리기
cv.circle(img, (320,240), 100, (255,0,0), 3)

# 타원그리기
cv.ellipse(img, (320,240), (300, 100), 0, 0, 360, (0,255,255), 2)
#                위치     장축   단축  기울기, 시작지점부터 도착지점까지의 도 표현

# 다각형그리기
pts = np.array([[50, 150], [200, 80], [350, 120], [300,200]], np.int32)
cv.polylines(img, [pts.reshape((-1,1,2))], True, (255,255,255), 2)
#   다각형 정의  함수에 맞는 형태로 재구성(고정된 배열), 닫혀있는형태일지 지정

# 채워진 다각형 만들기
pts = np.array([[50, 15], [200, 100], [350, 20], [300,200]], np.int32)
cv.fillPoly(img, [pts.reshape((-1,1,2))], (255,255,255))

# 텍스트 넣기
cv.putText(img, 'yeah', (10, 450), cv.FONT_HERSHEY_SIMPLEX, 4, (255,255,0),3)
                                #  폰트 지정                크기  색       굵기

cv.imshow('img', img)
cv.waitKey()