import cv2 as cv

capture = cv.VideoCapture(0)
# 카메라 번호지정
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv.CAP_PROP_FPS)
print('width, height = ', width, height, fps)

fourcc = cv.VideoWriter_fourcc(*'XVID')
# 코덱 설정
writer = cv.VideoWriter('capture.avi', fourcc, 30, (640, 480))

while True:
    ret, frame = capture.read()
    #ret = 리턴값을 받았는지의 유무(TRUE, FALSE), frame = 실제 이미지값
    writer.write(frame)
    # 프레임 저장
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27: break
    #반복문 탈출



capture.release()
writer.release()
# 자원 해제