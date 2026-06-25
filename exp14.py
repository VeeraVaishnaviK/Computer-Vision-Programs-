import cv2
import numpy as np

if __name__ == '__main__':
    # Load source and destination images
    im_src = cv2.imread(r"C:\Users\vaish\Downloads\tree.jpg")
    im_dst = cv2.imread(r"C:\Users\vaish\Downloads\tree.jpg")
    
    if im_src is None or im_dst is None:
        print("Error: Could not load the images. Please check the file path.")
        exit(1)
        
    # Get dimensions of source image (tree.jpg)
    h_src, w_src = im_src.shape[:2]
    
    # Source points (four corners of the source image)
    # Using the image corners ensures the entire tree image is warped,
    # preventing black/empty output since the original coordinates went up to 630.
    pts_src = np.array([[0, 0], [w_src - 1, 0], [w_src - 1, h_src - 1], [0, h_src - 1]], dtype=np.float32)
    
    # Destination points (four corners in the destination image where the source will be warped to)
    pts_dst = np.array([[318, 256], [534, 372], [316, 670], [73, 473]], dtype=np.float32)
    
    # Calculate homography matrix
    h, status = cv2.findHomography(pts_src, pts_dst)
    
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))
    
    # Resize for a cleaner consolidated display
    display_width = 400
    display_height = int(im_dst.shape[0] * (display_width / im_dst.shape[1]))
    
    im_src_resized = cv2.resize(im_src, (display_width, display_height))
    im_dst_resized = cv2.resize(im_dst, (display_width, display_height))
    im_out_resized = cv2.resize(im_out, (display_width, display_height))
    
    # Create comparison grid
    comparison = np.hstack((im_src_resized, im_dst_resized, im_out_resized))
    
    # Display images
    cv2.imshow("Homography Warp Comparison (Source | Destination | Warped)", comparison)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
