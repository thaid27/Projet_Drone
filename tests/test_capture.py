from utils.drone import init_drone
import cv2
from PIL import Image

tello = init_drone()
frame = tello.get_frame_read().frame
frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
image = Image.fromarray(frame_rgb)