import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("./image/cat.jpg",cv2.IMREAD_COLOR)

for ksize in (3,5,7,11) :
    dst1 = cv2.GaussianBlur(src,(ksize,ksize),0)
    desc = "Mean: {}*{}".format(ksize,ksize)
    cv2.putText(dst1,desc,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0,255 ,1, cv2.LINE_AA)
    cv2.imshow("dst1",dst1)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()