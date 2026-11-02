import cv2
import numpy as np
img = cv2.imread("./image/Lenna.png")

rows,cols,ch = img.shape
pts1 = np.float32([[220,260],[300,265],[270,340]])
pts2 = np.float32([[240,280],[340,270],[290,370]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img , M (cols,rows))

img_points = img.copy()
dst_points = dst.copy()

for pt in pts1 :
    cv2.circle(img_points, tuple(pt.astype(int)),6,(0,0,255),-1)

for pt in pts2:
    cv2. circle(dst_points, tuple(pt.astype(int)),6,(225,0,0),-1)