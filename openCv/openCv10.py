import cv2

# Set the desired width, height, and FPS
width = 640
height = 480
fps = 30

def callBack1(val):
    print(f'xPs {val}')
    
    
def callBack2(val):
    print(f'yPos {val}')    
    
# Open the default camera
cam = cv2.VideoCapture(0)

# Set camera properties
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('trackBars')
cv2.resizeWindow('trackBars', 600, 600)
cv2.moveWindow('trackBars', width, 0)

cv2.createTrackbar('xPos', 'trackBars', 0, 1920, callBack1)
cv2.createTrackbar('yPos', 'trackBars', 0, 1920, callBack2)

while True:
    # Read a frame from the camera
    ret, frame = cam.read()
    
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
