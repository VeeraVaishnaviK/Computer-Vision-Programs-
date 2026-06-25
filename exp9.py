import cv2

def play_video(video_path, speed=1.0):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file: {video_path}")
        return
        
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30.0  # Fallback FPS
        
    # We let cv2.imshow handle window sizing automatically,
    # which avoids asynchronous window destruction/recreation errors on Windows.
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        cv2.imshow("Video", frame)
        
        # Calculate delay based on FPS and speed multiplier
        delay = max(1, int(1000 / (fps * speed)))
        
        # Press ESC to exit
        if cv2.waitKey(delay) & 0xFF == 27:
            break
            
    cap.release()
    cv2.destroyAllWindows()

# Run the video player at different speeds
video_file = r"C:\Users\vaish\Downloads\flower vd.mp4"
print("Playing video at normal speed (1.0x)...")
play_video(video_file, speed=1.0)

print("Playing video at slow speed (0.5x)...")
play_video(video_file, speed=0.5)

print("Playing video at fast speed (3.0x)...")
play_video(video_file, speed=3.0)