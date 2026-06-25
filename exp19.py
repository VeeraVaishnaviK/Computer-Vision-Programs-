import cv2
import numpy as np

img = cv2.imread(r"C:\Users\vaish\Downloads\tree.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Sobel X", cv2.WINDOW_NORMAL)
cv2.namedWindow("Sobel Y", cv2.WINDOW_NORMAL)
cv2.namedWindow("Combined Sobel", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Combined Sobel", sobel_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()