import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("./image/scaned_paper.jpg",cv2.IMREAD_GRAYSCALE)
_,t_130 = cv2.threshold(img , 130 , 255, cv2.THRESH_BINARY)

t, t_otsu = cv2.threshold(img, -1 , 255 , cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print("otsu threshold:",t)

imgs = {"original":img, "t:100": t_130 ,"otwu:%d"%t:t_otsu}

plt.figure(figsize = (12,5))
for i , (key,value) in enumerate ( imgs.items()):
    plt.subplot(1,3,i+1)
    plt.title(key)
    plt.imshow(value,cmap= "gray")
    plt. xticks([]);plt.yticks([])

plt.show()