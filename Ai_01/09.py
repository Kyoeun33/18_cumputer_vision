import cv2

src = cv2.imread("./Ai_01/image/song_1.jpg", cv2.IMREAD_COLOR)
# 해당 이미지의 높이 , 너비, 채널의 값을 저장
height, width, channel = src.shape

dst_pyrUp = cv2.pyrUp(src, dstsize=(width * 2 , height *2),
                      borderType=cv2.BORDER_DEFAULT)
dst_Down = cv2.pyrDown(src)

cv2.imshow("src",src)
cv2.imshow("pyrUp",dst_pyrUp)
cv2.imshow("pyrDown",dst_Down)
cv2.waitKey()
cv2.destroyAllWindows()