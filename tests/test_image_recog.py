from PIL import Image
from utils.visual_recog import choix_image

# Test de reconnassances entre 3 images
image_paths = ["images/chien.jpg", "images/voiture.jpg", "images/pomme.jpg"]
images = [Image.open(path).convert("RGB") for path in image_paths]

mot = "chien"
image_resultat = choix_image(mot, images)
print(f"L'image qui correspond le mieux au mot '{mot}' est : {image_resultat}")