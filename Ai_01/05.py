import cv2

capture = cv2.VideoCapture("./Ai_01/youquiz.mp4")
print(capture.get(cv2.CAP_PROP_POS_FRAMES))
print(capture.get(cv2.CAP_PROP_FRAME_COUNT))

while cv2.waitKey(33) < 0 : # -1을 반환
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES,value = 0 )

    ret,frame = capture.read()
    cv2.imshow("wildlife",frame)

capture.release()
cv2.destroyAllWindows()

    ##망