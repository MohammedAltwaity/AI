import cv2

#multiple windows
width = 500
height = 500
fps = 30


rows = int(input('enter the number of rows.. '))
columns = int(input('enter the number of columns.. '))
# Open the default camera
cam = cv2.VideoCapture(0)

# Set camera properties ..
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


#ask the usr for the rows & columns


while True:
    ret, frame = cam.read()
    frame = cv2.resize(frame, (int(width/columns), int(height/columns)))
    if not ret:
        print("Error: Could not read frame.")
        break

    for i in range(rows):
        for j in range(columns):
            windowName = 'window' + str(i)+str(j)
            cv2.imshow(windowName,frame)
            cv2.moveWindow(windowName,int(width/columns)*j, int(height/columns)*i)
            
    
    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
