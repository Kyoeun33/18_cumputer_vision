import cv2

capture = cv2 . VideoCapture(0) # 카메라 열기
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 프레임 가로 길이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # 프레임 세로 길이
while cv2.waitKey(33) < 0 :
    ret, frame = capture.read()
    cv2.imshow("VedioFrame",frame) # 윈도우 창에 이름 출력 ("윈도우창 이름", 윈도우 창에 할당할 이미지를 의미)

capture.release()
cv2.destroyALLWindows() # winname을 가진 창만 닫는 다