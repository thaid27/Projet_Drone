from utils.drone import init_drone
import cv2
from PIL import Image
import time


tello = init_drone()
print("Initialisation")

frame_read = tello.get_frame_read()
time.sleep(1)  # Wait for stream to initialize

frame = frame_read.frame
# # Wait for a valid (non-black) frame
# for _ in range(30):
#     frame = frame_read.frame
#     if frame is not None and frame.sum() != 0:
#         break
#     time.sleep(0.1)
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
cv2.imwrite("image_drone.png", frame_rgb)


tello.streamoff()

print("Image enregistrée")
