import datetime
import cv2


capture = cv2.VideoCapture("./Ai_01/youquiz.mp4")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
record = False
while True :
    if(capture . get(cv2.CAP_PROP_POS_FRAMES)==capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("./Ai_01/youquiz.mp4")
    ret,frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    now = datetime.datetime.now().strftime("%d_%H_%M_%S")
    key = cv2.waitKey(33)
    print("key =>", key)

# 27 :Esc, 49 : 1(숫자), 50 :2(숫자) , 51: 3(숫자)

    if key == 27 :
        break
    elif key == 49:
        print("캡쳐")
        cv2.imwrite("./Ai_01/capture/"+str(now)+".png",frame)
    elif key == 50 :
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("./Ai_01/capture/" + str(now) + ".avi",fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 51 :
        print("녹화 중지")
        record = False
        video.release()

    if record == True :
        print("녹화중..")
        video.write(frame)


capture.release()
cv2.destroyAllWindows()