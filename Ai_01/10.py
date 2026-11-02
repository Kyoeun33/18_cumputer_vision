import cv2

img = cv2.imread("./Ai_01/image/cat.jpg")

dst_pyrUp = cv2.pyrUp(img)
dst_pyDown = cv2.pyrDown(img)

cv2.imshow("img",img)
cv2.imshow("pyrUp",dst_pyrUp)
cv2.imshow("pryDown",dst_pyDown)
cv2.waitKey()
cv2.destroyAllWindows()