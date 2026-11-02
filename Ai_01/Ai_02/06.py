import cv2 

src = cv2.imread("./image/duck.jpg",cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# 픽셀 값이 100을 초과하면 255, 이하면 0
ret, dst = cv2.threshold(gray, 100, 255 , cv2.THRESH_BINARY)
dst = cv2.resize(dst ,None,fx=1/3 , fy = 1/3 , interpolation= cv2.INTER_AREA)
src = cv2.resize(src ,None,fx=1/3 , fy = 1/3 , interpolation= cv2.INTER_AREA)

cv2.imshow("dst",dst)
cv2.imshow("srd",src)
cv2.waitKey()
cv2.destroyAllWindows()