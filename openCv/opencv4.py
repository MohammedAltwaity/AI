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

while True:
    # Read a frame from the camera
    ret, frame = cam.read()
     # Draw a red rectangle around a portion of the frame
    top_left = (240, 180)  # (x, y)
    bottom_right = (400, 300)  # (x, y)
    color = (0, 0, 255)  # Red in BGR
    thickness = 2  # Thickness of the rectangle border
    cv2.rectangle(frame, top_left, bottom_right, color, thickness)
    cv2.circle(frame, (int(width/2), int(height/2)), 50, color, -1)
    cv2.putText(frame, 'hello', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
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
