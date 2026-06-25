import cv2

# Read the main image (the flower)
main_image = cv2.imread("C:/Users/vaish/Downloads/Gnaphalium_affine.JPG")

if main_image is not None:
    main_height, main_width, _ = main_image.shape
    crop_height, crop_width = 80, 288
    
    # Crop a region of size 80x288 from the main image
    cropped_region = main_image[0:crop_height, 0:crop_width]
    
    # Read the image onto which we want to paste the cropped region
    paste_image = cv2.imread("C:/Users/vaish/Downloads/tree.jpg")
    
    if paste_image is not None:
        paste_height, paste_width, _ = paste_image.shape
        
        # Calculate coordinates to paste the cropped region at the bottom-right of paste_image
        paste_y = paste_height - crop_height
        paste_x = paste_width - crop_width
        
        # Paste the cropped region onto paste_image
        paste_image[paste_y:paste_height, paste_x:paste_width] = cropped_region
        
        # Display the result (paste_image with the cropped region inserted)
        cv2.imshow("Result", paste_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Could not load paste image.")
else:
    print("Error: Could not load main image.")
