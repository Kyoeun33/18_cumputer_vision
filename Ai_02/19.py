import cv2
import numpy as np

src = np.full((768,1366,3),255,dtype=np.uint8)

cv2.putText(src,"Plain",(50,30), cv2.FONT_HERSHEY_PLAIN,1,(0,0,0))
cv2.putText(src,"Simplex",(50,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
cv2.putText(src,"Duplex",(50,110),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0))
cv2.putText(src,"Simplex",(200,110),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))
cv2.putText(src,"Complex small",(50,220),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0))
cv2.putText(src,"Complex ",(50,260),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
cv2.putText(src,"Triplex",(200,260),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,0))
cv2.putText(src,"script simplex",(50,330),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,0,0))
cv2.putText(src,"script complex",(50,370),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,0,0))
cv2.putText(src,"plain italic",(50,430),cv2.FONT_HERSHEY_PLAIN |cv2.FONT_ITALIC,1,(0,0,0))
cv2.putText(src,"complex italic",(50,470),cv2.FONT_HERSHEY_COMPLEX|cv2.FONT_ITALIC,1,(0,0,0))

cv2.imshow("draw text", src)
cv2.waitKey()
cv2.destroyAllWindows()