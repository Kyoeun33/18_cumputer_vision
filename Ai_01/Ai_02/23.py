
import cv2
import numpy as np
import math

# ==========================================
# 1. 파일 경로
# ==========================================

VIDEO_PATH = "./image/solidWhiteRight.mp4"
REFERENCE_PATH = "./image/solidWhiteRight.png"
OUTPUT_PATH = "result_red_lines.mp4"


# ==========================================
# 2. 차선 검출 함수
# ==========================================

def detect_lines(image, reference=False):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    h, w = gray.shape

    if not reference:
        # 동영상에서 도로 영역만 추출
        mask = np.zeros_like(edges)

        polygon = np.array([[
            (int(w * 0.05), h),
            (int(w * 0.45), int(h * 0.58)),
            (int(w * 0.55), int(h * 0.58)),
            (w, h)
        ]], dtype=np.int32)

        cv2.fillPoly(mask, polygon, 255)
        edges = cv2.bitwise_and(edges, mask)

    # Hough 변환
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=15 if reference else 20,
        minLineLength=10 if reference else 20,
        maxLineGap=20 if reference else 30
    )

    if lines is None:
        return []

    result = []

    for line in lines:
        x1, y1, x2, y2 = line[0]

        # 기준 이미지의 좌측 테두리 노이즈 제거
        if reference and max(x1, x2) < w * 0.04:
            continue

        result.append((x1, y1, x2, y2))

    return result


# ==========================================
# 3. 선분의 기울기 계산
# ==========================================

def get_angle(line):

    x1, y1, x2, y2 = line

    angle = math.degrees(
        math.atan2(y2 - y1, x2 - x1)
    )

    return angle


# ==========================================
# 4. 두 선분의 일치 여부 확인
# ==========================================

def is_matching(reference_line, video_line, width, height):

    # 기울기 비교
    angle1 = get_angle(reference_line)
    angle2 = get_angle(video_line)

    angle_diff = abs(angle1 - angle2)
    angle_diff = min(angle_diff, 180 - angle_diff)

    if angle_diff > 12:
        return False

    # 각 선분의 중심 좌표
    def midpoint(line):
        x1, y1, x2, y2 = line
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    mx1, my1 = midpoint(reference_line)
    mx2, my2 = midpoint(video_line)

    # 이미지 크기가 달라도 비교할 수 있도록 정규화
    distance = math.sqrt(
        ((mx1 - mx2) / width) ** 2 +
        ((my1 - my2) / height) ** 2
    )

    if distance > 0.12:
        return False

    # 선분 길이 비교
    def length(line):
        x1, y1, x2, y2 = line
        return math.sqrt(
            (x2 - x1) ** 2 + (y2 - y1) ** 2
        )

    len1 = length(reference_line)
    len2 = length(video_line)

    ratio = len2 / max(len1, 1)

    if ratio < 0.25 or ratio > 4:
        return False

    return True


# ==========================================
# 5. 기준 이미지에서 차선 추출
# ==========================================

reference = cv2.imread(REFERENCE_PATH)

if reference is None:
    raise FileNotFoundError("기준 이미지를 찾을 수 없습니다.")

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    raise FileNotFoundError("동영상을 열 수 없습니다.")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 기준 이미지 크기를 동영상과 동일하게 변경
reference = cv2.resize(reference, (width, height))

reference_lines = detect_lines(reference, reference=True)

print("기준 이미지에서 검출한 선분:", len(reference_lines))


# ==========================================
# 6. 결과 동영상 생성
# ==========================================

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(
    OUTPUT_PATH,
    fourcc,
    fps,
    (width, height)
)

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # 현재 프레임에서 차선 추출
    video_lines = detect_lines(frame)

    matched_count = 0

    # 기준 이미지와 동영상의 선분 비교
    for video_line in video_lines:

        matched = False

        for ref_line in reference_lines:

            if is_matching(
                ref_line,
                video_line,
                width,
                height
            ):
                matched = True
                break

        # 일치하는 선분을 빨간색으로 표시
        if matched:

            x1, y1, x2, y2 = video_line

            cv2.line(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 0, 255),
                5
            )

            matched_count += 1

    # 일치하는 선분 개수 표시
    cv2.putText(
        frame,
        f"Matched Lines: {matched_count}",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    out.write(frame)

    frame_count += 1

    cv2.imshow("Lane Matching", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# ==========================================
# 7. 종료
# ==========================================

cap.release()
out.release()
cv2.destroyAllWindows()

print("분석 완료!")
print("저장 위치:", OUTPUT_PATH)
