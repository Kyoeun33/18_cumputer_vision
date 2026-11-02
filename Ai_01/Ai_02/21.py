import cv2
import numpy as np

src = cv2.imread("./image/solidWhiteCurve.jpg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, (0, 0, 200), (255, 30, 255))   # 채도 낮고, 밝은 부분 = 흰색
white = cv2.bitwise_and(hsv, hsv, mask=mask)
white = cv2.cvtColor(white, cv2.COLOR_HSV2BGR)

h, w = white.shape[:2]

# 사다리꼴 꼭짓점 (왼쪽 아래 → 왼쪽 위 → 오른쪽 위 → 오른쪽 아래)
pts = np.array([[0, h],
                [int(w * 0.50), int(h * 0.58)],   # 왼쪽 위: 가운데(0.5)
                [int(w * 0.58), int(h * 0.58)],   # 오른쪽 위: 가운데에서 0.08 오른쪽
                [w, h]], dtype=np.int32)

roi = np.zeros((h, w), dtype=np.uint8)            # 검은 화면 (흑백)
cv2.fillPoly(roi, [pts], 255)                     # 사다리꼴만 흰색으로 채움
result = cv2.bitwise_and(white, white, mask=roi)  # 사다리꼴 안만 남김

# 원본에 자르는 위치 표시해서 확인
check = src.copy()
cv2.polylines(check, [pts], True, (0, 0, 255), 2)

cv2.imshow("check", check)
cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()