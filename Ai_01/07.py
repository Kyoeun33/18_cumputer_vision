import cv2

src = cv2.imread("./Ai_01/image/cat.jpg",cv2.IMREAD_COLOR)

dst = cv2.flip(src, 0 )
dst1 = cv2.flip(src, 1)
dst2 = cv2.flip(src , -1)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()