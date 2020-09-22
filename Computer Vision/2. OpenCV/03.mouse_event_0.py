import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)


def on_mouse(event, x, y, flags, param):
    print(event, x, y, flags, param)


cv.namedWindow('img')
cv.setMouseCallback('img', on_mouse)


# 아무 입력없는 창 생성

# cv.imshow('img', img)
cv.waitKey()
