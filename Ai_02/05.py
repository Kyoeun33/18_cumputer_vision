import cv2

src = cv2.imread("./image/bird.jpg",cv2.IMREAD_COLOR)
dst = cv2.bitwise_not(src)

src = cv2.resize(src,None,fx=1/3 , fy = 1/3 , interpolation= cv2.INTER_LINEAR)
dst = cv2.resize(dst ,None,fx=1/3 , fy = 1/3 , interpolation= cv2.INTER_LINEAR)

cv2.imshow("src", src)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()