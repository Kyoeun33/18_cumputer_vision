# https://m.blog.naver.com/PostView.naver?blogId=windowsub0406&logNo=220893893795&targetKeyword=&targetRecommendationCode=1
# 동영상에 적용
import cv2  # opencv 사용
import numpy as np

def region_of_interest(img, vertices, color=(255, 255, 255)):  # ROI 셋팅

    mask = np.zeros_like(img)  # mask = img와 같은 크기의 빈 이미지

    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움
    cv2.fillPoly(mask, vertices, color)

    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image


def mark_img(img, blue_threshold=200, green_threshold=200, red_threshold=200):  # 흰색 차선 찾기

    #  BGR 제한 값
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (image[:, :, 0] < bgr_threshold[0]) \
                 | (image[:, :, 1] < bgr_threshold[1]) \
                 | (image[:, :, 2] < bgr_threshold[2])
    img[thresholds] = [0, 0, 0]
    return img


cap = cv2.VideoCapture('./images/solidWhiteRight.mp4')  # 동영상 불러오기

while (cap.isOpened()):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, image = cap.read()
    height, width = image.shape[:2]  # 이미지 높이, 너비

    # 사다리꼴 모형의 Points
    vertices = np.array(
        [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60), (width - 50, height)]],
        dtype=np.int32)
    roi_img = region_of_interest(image, vertices, (0, 0, 255))  # vertices에 정한 점들 기준으로 ROI 이미지 생성

    mark = np.copy(roi_img)  # roi_img 복사
    mark = mark_img(mark)  # 흰색 차선 찾기

    # 흰색 차선 검출한 부분을 원본 image에 overlap 하기
    color_thresholds = (mark[:, :, 0] == 0) & (mark[:, :, 1] == 0) & (mark[:, :, 2] > 200)
    image[color_thresholds] = [0, 0, 255]

    cv2.imshow('results', image)  # 이미지 출력
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release
cap.release()
cv2.destroyAllWindows()