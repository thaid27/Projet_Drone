import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel


# Fonction pour reconnaitre l'image correspondant au texte de l'utilisateur
def choix_image(text_prompt, images):

    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

    # Charger le modèle et le processor CLIP pour la reconnaissance d'image
    model = CLIPModel.from_pretrained("./models/clip-vit-base-patch32", use_safetensors=True).to(device)
    processor = CLIPProcessor.from_pretrained("./models/clip-vit-base-patch32")

    # Charger les images
    inputs = processor(text=[text_prompt], images=images, return_tensors="pt", padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)
        logits_per_image = outputs.logits_per_image  # [num_images, num_texts]
        probs = logits_per_image.softmax(dim=0)

    # Trouver l'image avec la proba la plus forte
    best_index = probs.argmax().item()
    return best_index, probs.cpu().tolist()



