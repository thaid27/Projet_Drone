# Script principale pour faire voler le robot, reconnaitre l'image indiqué par l'utilisateur et le faire atterrir devantframe = tello.get_frame_read().frame
from utils.drone import init_drone, get_images, land_under_image
from utils.visual_recog import choix_image
import time
import cv2
import threading

# Paramètres modifiables
text_prompt = "chien" # ou "pomme", "voiture" 

hauteur_images = 100
distance_btw_images = 120 # à calibrer en fonction de la situation
distance_mur = 20  # à calibrer en fonction de la situation
nb_images = 3  

# Paramètres video
video_filename = "images_capt/mission_video.mp4"
fps = 30
width, height = 960, 720


# Connection au drone
tello = init_drone() 
frame_read = tello.get_frame_read()

# Lancer l'enregistrement vidéo en parallèle
video_writer = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
print("Connexion OK - Enregistrement vidéo lancé")

def record_video():
    while tello.stream_on:
        frame = frame_read.frame
        resized = cv2.resize(frame, (width, height))
        frame_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        video_writer.write(frame_rgb)
        time.sleep(1 / fps)

record_thread = threading.Thread(target=record_video)
record_thread.start()


# Décollage de drone
tello.takeoff()
tello.move_up(hauteur_images)
time.sleep(2)
print("Décollage")

# Scan des images sur le murs
images = get_images(tello, nb_images, distance_btw_images)
print("Capture d'images")

# Identification de l'image correspondant au prompt utilisateur
index_choix, score_list = choix_image(text_prompt, images)
print("Analyse des Images")
print(f"Score list :{score_list}, Index image choisie {index_choix}") # 

# Déplacement vers l'image correspondant 
index_to_go = nb_images - 1 - index_choix # nb_images - 1 = index image tout à droite
tello.move_left(index_to_go * distance_btw_images)
time.sleep(2)
print("déplacement vers l'image choisie")

# Atterrir devant l'image
land_under_image(tello, distance_mur)
print("Atterrissage")

time.sleep(1)
video_writer.release()
cv2.destroyAllWindows()
tello.streamoff()
tello.end()
print(f"Vidéo enregistrée dans {video_filename}")