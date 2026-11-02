import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("./image/cat.jpg",cv2.IMREAD_COLOR)
dst = cv2.GaussianBlur(src,(9,9),0)
# sigamX : 가우시안 블러의 강도를 결정하는 표준 편차
# 주변 픽셀의 밝기를 계산할떄 중심 픽셀에서 얼마나 넓은 범위까지 영향을 줄 것인지를 결정하는 값

cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()
