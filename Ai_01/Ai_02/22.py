
import cv2
import numpy as np

# ==========================================
# 2. 동영상 불러오기
# ==========================================

cap = cv2.VideoCapture("./image/solidWhiteRight.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"DIVX")

out = cv2.VideoWriter(
    "result.mp4",
    fourcc,
    fps,
    (w, h)
)


# ==========================================
# 3. ROI 영역 설정
# ==========================================

# 과제2 작성한 사다리꼴 좌표 그대로 활용--> 흰색 사다리꼴 만들기
pts = np.array([
    [0, h],
    [int(w * 0.50), int(h * 0.58)],
    [int(w * 0.58), int(h * 0.58)],
    [w, h]
], dtype=np.int32)

roi = np.zeros((h, w), dtype=np.uint8)
cv2.fillPoly(roi, [pts], 255)

# ==========================================
# 4. 동영상 프레임별 처리
# ==========================================


while True:
    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    # BGR -> HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 흰색 검출
    mask = cv2.inRange(
        hsv,
        (0, 0, 200),
        (255, 30, 255)
    )

    # ROI 영역만 남기기
    roi_mask = cv2.bitwise_and(
        mask,
        mask,
        mask=roi
    )

    # ======================================
    # 5. 검출된 흰색 차선을 빨간색으로 변경
    # ======================================

    output = frame.copy()
    # 빨간색 = (0, 0, 255)
    output[roi_mask > 0] = (0, 0, 255)

    # 결과 저장
    out.write(output)
    cv2.imshow("Output", output)

    # ESC 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# ==========================================
# 6. 종료 및 저장
# ==========================================

cap.release()
out.release()
cv2.destroyAllWindows()

