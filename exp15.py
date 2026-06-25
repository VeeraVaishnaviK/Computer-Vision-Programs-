import cv2
import numpy as np

# Load images
img1 = cv2.imread(r"C:\Users\vaish\Downloads\Gnaphalium_affine.JPG")
img2 = cv2.imread(r"C:\Users\vaish\Downloads\tree.jpg")

if img1 is None or img2 is None:
    print("Error: Could not load the images. Please check the paths.")
    exit(1)

# Get dimensions of both images
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

# Define corresponding points as the four corners of the images
# This warps the entire img1 onto the entire shape of img2
pts1 = np.float32([[0, 0], [w1 - 1, 0], [0, h1 - 1], [w1 - 1, h1 - 1]])
pts2 = np.float32([[0, 0], [w2 - 1, 0], [0, h2 - 1], [w2 - 1, h2 - 1]])

# Calculate Homography matrix H
H, status = cv2.findHomography(pts1, pts2)

# Warp img1 to img2's perspective using homography
dst = cv2.warpPerspective(img1, H, (w2, h2))

# Resize img1 for a cleaner display on the screen (since the original is 1280x853)
img1_resized = cv2.resize(img1, (w2, h2))

# Create a side-by-side comparison of: [Resized Source, Destination, Warped Result]
comparison = np.hstack((img1_resized, img2, dst))

# Create a blended version (50% destination, 50% warped source)
blended = cv2.addWeighted(img2, 0.5, dst, 0.5, 0)

# Display the images
cv2.imshow('Comparison (Source | Destination | Warped)', comparison)
cv2.imshow('Blended (Destination + Warped)', blended)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 16. Perform Edge detection using canny method
