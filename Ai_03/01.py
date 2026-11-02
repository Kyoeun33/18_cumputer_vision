import cv2

img = cv2.imread("./image/sunset.jpg")

x = 320 
y= 150
w = 50
h = 50

roi = img[ y:y+h , x: x+w]

print ( roi.shape)
cv2.rectangle(roi,(0,0),(h-1,w-1),(0,225,0))
cv2.imshow("img ", img)

key = cv2.waitKey()
print(key)
cv2.destroyAllWindows()