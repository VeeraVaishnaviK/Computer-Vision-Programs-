import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\vaish\Downloads\tree.jpg")

if image is None:
    print("Error: Could not load the image.")
    exit(1)

# Get image dimensions
height, width = image.shape[:2]

x = 100
y = 100
dx = 50
dy = 30

while True:
    # Create the translation matrix using x and y
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    
    # Translate the image
    image_copy = cv2.warpAffine(image, translation_matrix, (width, height))
    
    # Display the translated image
    cv2.imshow('Moving Image', image_copy)
    
    # Wait for 200 ms. If user presses 'q' or 'ESC', break the loop.
    key = cv2.waitKey(200) & 0xFF
    if key == 27 or key == ord('q'):
        break
        
    # Increment position
    x += dx
    y += dy
    
    # Reset coordinates if the image moves completely off screen
    if x > width or y > height:
        x = 0
        y = 0

cv2.destroyAllWindows()