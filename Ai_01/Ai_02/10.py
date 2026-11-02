import cv2 
import matplotlib.pyplot as plt

blk_size  = 9 # 블럭 사이즈 : 픽셀의 임계값으 계산할 떄 참고하는 영역의 크기(홀수만 된다고 함)
                                                        # 주변 1칸 | 현재 픽셀 | 주변 1칸
c = 5 # 차감 상수 : 주변 영역의 평균 밝기 또는 가우시안 가중 평균으로 계산한 임계값에서 빼는 보정 상수


img = cv2.imread("./image/sudoku.jpg",cv2.IMREAD_GRAYSCALE)# -오츠의 알고리즘으로 단일 경계값을 전체 이미지에 적용

ret,th1 = cv2.threshold(img , 0 , 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 어뎁티드 쓰레쉬 홀드 산술 평균과 가우시란 분포로 각각 적용
th2 = cv2 . adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,blk_size,c)
th3 = cv2 . adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,blk_size,c)

imgs = { "original" : img , "Global - Otsu:%d" %ret:th1 ,
        "Adapted - Mean" : th2 , "Adapted - Gaussian" : th3}

for i , (k,v) in enumerate ( imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v,cmap= "gray")
    plt. xticks([]);plt.yticks([])

plt.show()