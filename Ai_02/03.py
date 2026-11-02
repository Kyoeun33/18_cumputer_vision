import cv2

src = cv2.imread("./image/chess.jpg",cv2.IMREAD_COLOR)


dst = src.copy()
roi = src[100:600 , 200:700]
dst[0:500 , 0:500] = roi

src = cv2.resize(src , None , fx = 1/2, fy = 1/2, interpolation=cv2.INTER_AREA)
dst = cv2.resize(dst , None , fx = 1/2, fy = 1/2, interpolation=cv2.INTER_AREA)

cv2.imshow("src", src)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()