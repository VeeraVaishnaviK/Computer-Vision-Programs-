import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue
        
    # Draw tracking points on the frame
    cv2.circle(frame, (114, 151), 5, (0, 0, 255), -1)
    cv2.circle(frame, (605, 89), 5, (0, 0, 255), -1)
    cv2.circle(frame, (72, 420), 5, (0, 0, 255), -1)
    cv2.circle(frame, (637, 420), 5, (0, 0, 255), -1)
    
    imgPts = np.float32([[114, 151], [605, 89], [72, 420], [637, 420]])
    objPoints = np.float32([[0, 0], [420, 0], [0, 637], [420, 637]])
    
    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(imgPts, objPoints)
    result = cv2.warpPerspective(frame, matrix, (400, 600))
    
    # Display frames
    cv2.imshow('frame', frame)
    cv2.imshow('Perspective Transformation', result)
    
    # Wait for key press (1 ms)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
