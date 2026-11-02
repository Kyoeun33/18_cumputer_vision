## 과제
import cv2
import numpy as np

img = cv2.imread("../image/paper.jpg")

points = []
preview = img.copy()

def onMouse(event, x, y, flags, param):
    global preview, points

    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append([x, y])
        # 클릭한 위치에 원 표시
        cv2.circle(preview, (x, y), 6, (0, 0, 255), -1)
        cv2.imshow("picture",preview)

cv2.imshow("picture",img)
cv2.setMouseCallback("picture", onMouse)


while len(points) < 4:
    cv2.waitKey(1)


# 네 점의 좌표 추출
tl, tr, br, bl = np.float32(points)

# 가로와 세로 길이 계산
width = int(max(
    np.linalg.norm(tr - tl),
    np.linalg.norm(br - bl)
))

height = int(max(
    np.linalg.norm(bl - tl),
    np.linalg.norm(br - tr)
))
 
# 변환 후 목적지 좌표
destination = np.float32([
    [0, 0],
    [width - 1, 0],
    [width - 1, height - 1],
    [0, height - 1]
])

# 원근 변환 행렬
matrix = cv2.getPerspectiveTransform(
    np.float32(points), destination
)

# 원근 변환
warped = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Perspective transformed", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()