import cv2
import numpy as np
evt = 0
xVal = 0
yVal =0

def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global xVal, yVal
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        xVal = xPos
        yVal = yPos
        evt= event
    if event == cv2.EVENT_RBUTTONUP:
        print(event)
    
    
    
# Set the desired width, height, and FPS
width = 640
height = 480
fps = 30

# Open the default camera
cam = cv2.VideoCapture(0)

# Set camera properties
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('Camera')
cv2.setMouseCallback('Camera',mouseClick)

while True:
    # Read a frame from the camera
    ret, frame = cam.read()
    if evt == 1:
        x =np.zeros([250,250,3],dtype=np.uint8)
        y = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color = y[yVal][xVal]
        print(color)
        x[:,:] = color
        
        
        
        cv2.imshow('picker',x)
        cv2.moveWindow('picker', width + 40,0 )
        evt =0
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow('Camera', frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
