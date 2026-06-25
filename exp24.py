import cv2
import numpy as np

# Load original image and watermark image
img = cv2.imread("C:/Users/vaish/Downloads/tree.jpg")
wm = cv2.imread("C:/Users/vaish/Downloads/Gnaphalium_affine.JPG")

if img is None or wm is None:
    print("Error: Could not load the images. Please check the paths.")
    exit(1)

# Resize the images to appropriate dimensions
resized_img = cv2.resize(img, (600, 600))
resized_wm = cv2.resize(wm, (200, 200))

# Get dimensions of the resized image
h_img, w_img, _ = resized_img.shape
center_y = int(h_img / 2)
center_x = int(w_img / 2)

# Get dimensions of the watermark
h_wm, w_wm, _ = resized_wm.shape
top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm

# Crop the Region of Interest (ROI) from the center of the main image
roi = resized_img[top_y:bottom_y, left_x:right_x]

# Blend the ROI and the watermark
result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)

# Replace the ROI in the main image with the blended result
resized_img[top_y:bottom_y, left_x:right_x] = result

# Save the watermarked image
# NOTE: We save to "tree_watermarked.jpg" to avoid overwriting your original "tree.jpg"
filename = "C:/Users/vaish/Downloads/tree_watermarked.jpg"
cv2.imwrite(filename, resized_img)

# Display the result
cv2.imshow("Resized Input Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
