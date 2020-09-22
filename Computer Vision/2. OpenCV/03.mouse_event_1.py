import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)


def on_mouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)
    elif event == cv.EVENT_LBUTTONUP:
        print(x, y)
    elif event == cv.EVENT_LBUTTONDBLCLK:
        print(x, y)
    elif event == cv.EVENT_MOUSEHWHEEL:
        if flags > 0:
            print('mouse wheel scrolled down at', x, y)
        else:
            print('mouse wheel scrolled up at', x, y)

        # 휠 다운 감지(내릴떈 flags 값이 음수 올릴땐 양수)



cv.namedWindow('img')
# 아무 입력없는 창 생성

# 마우스 휠 스크롤 감지
cv.setMouseCallback('img', on_mouse)
cv.imshow('img', img)

cv.waitKey()