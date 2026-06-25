import cv2
import numpy as np

image = cv2.imread("C:/Users/vaish/Downloads/Gnaphalium_affine.JPG")
if image is not None:
    height, width = image.shape[:2]
    tx, ty = 100, 50
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Translated Image', translated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load the image.")

