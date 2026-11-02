import cv2
import numpy as np

win_name = "scanning"
img = cv2.imread("./images/paper.jpg")
rows, cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)

def onMouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x, y]
        pts_cnt += 1
        if pts_cnt == 4:
            print(pts)
            sm = pts.sum(axis=1)
            print(sm)
            diff = np.diff(pts, axis=1)
            print(diff)

            topLeft = pts[np.argmin(sm)]  # x+y가 가장 값이 좌상단 좌표
            bottomRight = pts[np.argmax(sm)]  # x+y가 가장 큰 값이 우하단 좌표
            topRight = pts[np.argmin(diff)]  # x-y가 가장 작은 것이 우상단 좌표
            bottomLeft = pts[np.argmax(diff)]  # x-y가 가장 큰 값이 좌하단 좌표
            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            w1 = abs(bottomRight[0] - bottomLeft[0])  # 상단 좌우 좌표간의 거리
            w2 = abs(topRight[0] - topLeft[0])  # 하단 좌우 좌표간의 거리
            h1 = abs(topRight[1] - bottomRight[1])  # 우측 상하 좌표간의 거리
            h2 = abs(topLeft[1] - bottomLeft[1])  # 좌측 상하 좌표간의 거리
            width = int(max([w1, w2]))  # 두 좌우 거리간의 최대값이 서류의 폭
            height = int(max([h1, h2]))  # 두 상하 거리간의 최대값이 서류의 높이

            pts2 = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])

            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (width, height))
            cv2.imshow('scanned', result)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
