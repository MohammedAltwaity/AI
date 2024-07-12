import numpy as np
import cv2

while True:
    frame = np.zeros([250,250], dtype=np.uint8)
    frame[:,:] = 125
    cv2.imshow('My Window', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break