# Projet_Drone

Le but de ce projet est de faire en sorte que le drone se déplace vers une image choisie parmi un set d'images prédéfinies accrochées sur un mur, horizontalement. Le drone utilisé est de la marque Tello et est équipé d'une caméra afin de capturer les différentes images.

Le projet se décompose en deux parties :
- Reconnaisance d'objets : Utilise les images capturées par le drone. Le modèle utilisé est CLIP d'openai effectuant un embedding de l'image dans un espace vectorielle capturant la sémantique image/texte
- Pilotage du drone : scannage du murs et capture d'images, déplacement vers l'image choisie

# Pour lancer le projet

- Installer les requirements
- Lancer le script setup.py qui va télécharger le modèle clip et le stocker dans le répertoire du projet
- Dans main.py adapter les paramètres à la disposition réelle de la situation (distance au mur, distance entre les images, choix de l'image, ...)
- python main.py lance tout le processus (décollage, scan et analyse d'images, atterrisage devant l'image choise)
- Pour lancer les tests : python -m tests.test_capture

# Remarques

- Les images capturées par le drone sont stockées dans le dossier images_capt
- Pour un bon fonctionnement du processus, veillez à bien écarter les images et les placer sur la même ligne, mettre le drone devant l'image tout à gauche, avoir de bonnes conditions lumineuses  