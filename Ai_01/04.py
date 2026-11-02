import cv2

img_file = "./Ai_01/image/yeosu.jpg"
img = cv2.imread(img_file, cv2.IMREAD_ANYCOLOR)

if img is not None :
    cv2.imshow("IMG",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else :
    print("no image files.")