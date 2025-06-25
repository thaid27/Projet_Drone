# Script principale pour faire voler le robot, reconnaitre l'image indiqué par l'utilisateur et le faire atterrir devantframe = tello.get_frame_read().frame
from utils.drone import init_drone, get_images, land_under_image
from utils.visual_recog import choix_image
import time

# Paramètres modifiables
text_prompt = "chien"
position_actuelle = 0
hauteur_images = 0
distance_btw_images = 50 # à calibrer en fonction de la situation
distance_mur = 100  # à calibrer en fonction de la situation
nb_images = 3  

# Connection au drone
tello = init_drone() 

# Décollage de drone
tello.takeoff()
tello.move_up(50)
time.sleep(2)
print("Décollage")

# Scan des images sur le murs
images = get_images(tello, nb_images, distance_btw_images)
print("Capture d'images")

# Identification de l'image correspondant au prompt utilisateur
index_choix = choix_image(text_prompt, images)
print("Analyse des Images")

# Déplacement vers l'image correspondant 
index_to_go = nb_images - 1 - index_choix # nb_images - 1 = index image tout à droite
tello.move_left(index_to_go * distance_btw_images)
time.sleep(2)
print("déplacement vers l'image choisie")

# Atterrir devant l'image
land_under_image(tello, distance_mur)
print("Atterrissage")