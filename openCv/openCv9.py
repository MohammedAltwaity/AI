import cv2
import numpy as np

x = np.zeros([256,180,3], dtype=np.uint8)

for row in range(0,256,1):
    for column in range(0,180,1):
        x[row,column] = (column,row,255)
         
        
x = cv2.cvtColor(x, cv2.COLOR_HSV2BGR)         
               
while True:
    cv2.imshow('HSV',x)
    cv2.moveWindow('HSV', 0, 0)
    
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()   