
import cv2
import numpy as np

src = cv2.imread("./images/solidWhiteCurve.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, (0, 0, 200), (255, 30, 255))   
white = cv2.bitwise_and(hsv, hsv, mask=mask)
white = cv2.cvtColor(white, cv2.COLOR_HSV2BGR)

h, w = white.shape[:2]
top = int(h * 0.55)

dst = white[top:h, 0:w].copy()          # ROI: 아래쪽 도로 부분만 잘라냄

result = np.zeros_like(white)           # 원본과 같은 크기의 검은 화면
result[top:h, 0:w] = dst                # 잘라낸 ROI를 같은 위치에 붙여 넣음

cv2.imshow("src", src)
cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()
