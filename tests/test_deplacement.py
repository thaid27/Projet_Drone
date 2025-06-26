from utils.drone import init_drone, land_under_image
import time

distance_to_wall = 50

tello = init_drone()
print("Initialisation")
tello.takeoff()
time.sleep(2)
land_under_image(tello, distance_to_wall)
print("Atterrisage")
tello.streamoff()
tello.end()