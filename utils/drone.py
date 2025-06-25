from djitellopy import Tello
import time
import cv2
from PIL import Image


# Connection avec le drone
def init_drone():
    tello = Tello()
    tello.connect()
    print(f"Battery level: {tello.get_battery()}%")
    tello.streamon()
    return tello 


# Fonction scan des trois images 
def get_images(tello, nb_images, distance_btw_images):
    images = []

    for i in range(nb_images):
        frame = tello.get_frame_read().frame
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)
        images.append(image)
        print(f"Image {i+1} capturée.")
        if i < 2:
            tello.move_right(distance_btw_images)
            time.sleep(2)

    return images


# Atterrissage en dessous de la dernière image capturée
def land_under_image(tello, distance_to_wall):

    tello.move_forward(distance_to_wall)
    time.sleep(2)
    tello.land()
