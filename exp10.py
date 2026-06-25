import cv2
import time

# Try DirectShow first (cv2.CAP_DSHOW), which is more stable on Windows and resolves MSMF grabbing errors
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    # Fallback to default backend
    cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera")
    exit()

cv2.namedWindow("Webcam Video")
speed_factor = 1.0

# Camera warmup loop to allow sensor exposure to adjust
for _ in range(10):
    ret, frame = cap.read()
    if ret and frame is not None:
        break
    time.sleep(0.1)

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        continue  # Keep trying if a frame fails to load temporarily
        
    cv2.imshow("Webcam Video", frame)
    
    # Calculate variable delay to simulate speed change in the preview loop
    delay = max(1, int(33 / speed_factor))
    key = cv2.waitKey(delay) & 0xFF
    
    if key == ord('+') or key == ord('='):
        speed_factor = min(10.0, speed_factor + 1.0)
        print(f"Speed factor increased: {speed_factor:.1f}x")
    elif key == ord('-') or key == ord('_'):
        speed_factor = max(0.2, speed_factor - 1.0)
        print(f"Speed factor decreased: {speed_factor:.1f}x")
    elif key == ord('q') or key == 27:  # 'q' or ESC to exit
        break
        
    # Attempt to set the hardware camera FPS (if supported by hardware)
    cap.set(cv2.CAP_PROP_FPS, 30 * speed_factor)

cap.release()
cv2.destroyAllWindows()