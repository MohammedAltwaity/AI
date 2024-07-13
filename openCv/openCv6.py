import time
import cv2

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

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    start = time.time()

    ret, frame = cam.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Define the Region of Interest (ROI)
    roi_width = 320
    roi_height = 240
    frameROI = frame[0:roi_height, 0:roi_width]
    frameRIOGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)

    # Display the ROI window
    cv2.imshow('my ROI gray', frameRIOGray)
    cv2.moveWindow('my ROI gray', 800, 0)
    
    
    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI', 650, 0)  # Corrected the window name here

    # Draw a rectangle on the main frame
    top_left = (240, 180)  # (x, y)
    bottom_right = (400, 300)  # (x, y)
    color = (0, 0, 255)  # Red in BGR
    thickness = 2  # Thickness of the rectangle border
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)

    # Draw a circle on the main frame
    cv2.circle(frame, (int(width / 2), int(height / 2)), 50, color, -1)

    # Calculate FPS
    dT = time.time() - start
    fps = 1 / dT if dT > 0 else 0

    # Put FPS text on the frame
    cv2.putText(frame, f"FPS: {int(fps)}", (0, 100), font, 2, (0, 0, 255), 3)

    # Display the main frame
    cv2.imshow('Camera', frame)

    # Print FPS
    print(f"FPS: {fps:.2f}")

    # Exit on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
