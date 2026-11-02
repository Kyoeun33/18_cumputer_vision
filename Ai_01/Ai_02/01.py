import cv2

src = cv2.imread("./image/cat.jpg",cv2.IMREAD_COLOR)

dst1 = cv2.resize(src, dsize = (800,600),interpolation=cv2.INTER_AREA)
dst2 = cv2.resize(src, dsize = (0,0),fx= 0.3 , fy = 0.7, interpolation= cv2.INTER_LINEAR)
dst3 = cv2.resize(src, dsize = (0,0),fx= 0.8 , fy = 1.7, interpolation= cv2.INTER_CUBIC)
dst4 = cv2.resize(src, dsize = (0,0),fx= 0.3 , fy = 0.7, interpolation= cv2.INTER_NEAREST)

cv2.imshow("src", src)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)
cv2.imshow("dst4",dst4)
cv2.waitKey()
cv2.destroyAllWindows()