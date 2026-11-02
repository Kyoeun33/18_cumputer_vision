import cv2


src = cv2.imread("./image/sudoku.jpg",cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1,0,3)
laplactian = cv2 . Laplacian(gray, cv2.CV_8U,ksize=3)
canny = cv2.Canny(src, 100,255)

src = cv2.resize(src, dsize=None , fx=1., fy=1., interpolation=cv2.INTER_AREA)
sobel = cv2.resize(sobel, dsize=None , fx=1., fy=1., interpolation=cv2.INTER_AREA)
laplactian = cv2.resize(laplactian, dsize=None , fx=1., fy=1., interpolation=cv2.INTER_AREA)
canny = cv2.resize(canny, dsize=None , fx=1., fy=1., interpolation=cv2.INTER_AREA)

cv2.imshow("src",src)
cv2.imshow("sobel",sobel)
cv2.imshow("laplaction",laplactian)
cv2.imshow("canny",canny) ## 얘가 잘 나옴 
cv2.waitKey()
cv2.destroyAllWindows()