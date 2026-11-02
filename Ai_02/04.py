import cv2

src = cv2.imread("./image/chess.jpg",cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

src = cv2.resize(src,None,fx = 1/3, fy = 1/3 ,interpolation=cv2.INTER_AREA)
dst = cv2.resize(dst,None,fx = 1/3, fy = 1/3 ,interpolation=cv2.INTER_AREA)

cv2.imshow("src", src)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()