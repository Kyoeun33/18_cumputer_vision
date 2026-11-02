import cv2

img = cv2.imread("./image/tomato.jpg", cv2.IMREAD_COLOR)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)


lower_red = cv2.inRange(hsv,(0,100,100),(5,255,255))
upper_red = cv2.inRange(hsv, (170, 100,100), (179, 255, 255))
added_red = cv2.addWeighted(lower_red, 1.0 , upper_red , 1.0,1)

red = cv2.bitwise_and(hsv,hsv, mask = added_red)
red =  cv2 . cvtColor(red, cv2.COLOR_HSV2BGR)

red1 = cv2.resize(lower_red, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)
red2 = cv2.resize(upper_red, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)
red3 = cv2.resize(added_red, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)


cv2.imshow("src" ,img)
cv2.imshow("red" ,red1)
cv2.imshow("red" ,red2)
cv2.imshow("red" ,red3)
cv2.waitKey()
cv2.destroyAllWindows()