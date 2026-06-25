import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\vaish\Downloads\tree.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian Mask
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Convert to uint8
laplacian = cv2.convertScaleAbs(laplacian)

# Sharpen the image
sharpened = cv2.subtract(gray, laplacian)

# Display results
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Laplacian Mask", cv2.WINDOW_NORMAL)
cv2.namedWindow("Sharpened Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", gray)
cv2.imshow("Laplacian Mask", laplacian)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()