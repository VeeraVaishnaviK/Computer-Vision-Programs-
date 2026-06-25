import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\vaish\Downloads\tree.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter along Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display images
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Sobel Y Edge Detection", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y Edge Detection", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()