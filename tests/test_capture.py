from utils.drone import init_drone
import cv2
from PIL import Image
import time


# Capture d'image avec la camera du drone
tello = init_drone()
print("Initialisation")

frame_read = tello.get_frame_read()
time.sleep(1)

frame = frame_read.frame
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
cv2.imwrite("iamges_capt/image_drone.png", frame_rgb)


tello.streamoff()

print("Image enregistrée")
