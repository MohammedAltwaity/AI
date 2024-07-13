import cv2

# Set the desired width, height, and FPS
width = 640
height = 480
fps = 30

#Setting the snip dims
snipW = .30 * width
snipH = .20 * height 


boxCR = int(height/2)
boxCC = int(width/2)


#move the box
deltaRow =1
deltaColumn = 1



# Open the default camera
cam = cv2.VideoCapture(0)

# Set camera properties
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    # Read a frame from the camera
    ret, frame = cam.read()
    frameRIO = frame[int(boxCR-snipH/2):int(boxCR+snipH/2), int(boxCC-snipW/2):int(boxCC+snipW/2)]
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[int(boxCR-snipH/2):int(boxCR+snipH/2), int(boxCC-snipW/2):int(boxCC+snipW/2)] = frameRIO
    
    if boxCR-snipH/2 <= 0 or boxCR+snipH/2 >= height:
        deltaRow = deltaRow *(-1)
    if boxCC-snipW/2 <= 0 or boxCC + snipW/2>=  width:
        deltaColumn = deltaColumn *(-1)
    
    boxCR = boxCR  + deltaRow
    boxCC = boxCC + deltaColumn
    
    
    cv2.imshow('my RIO',frameRIO)
    cv2.moveWindow('my RIO', width, 0)
    
    
     

    # Display the frame
    cv2.imshow('Camera', frame)
    
    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
