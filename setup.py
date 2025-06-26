from transformers import CLIPModel, CLIPProcessor
import os

import transformers.modeling_utils as modeling_utils

# Patch pour définir DTensor comme None globalement dans transformers
class DummyDTensor:
    pass

modeling_utils.DTensor = DummyDTensor

save_path = "./models/clip-vit-base-patch32"
os.makedirs(save_path, exist_ok=True)

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32", use_safetensors=True)
model.save_pretrained(save_path, safe_serialization=True)

processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
processor.save_pretrained(save_path)

print("✅ Modèle et processor sauvegardés localement dans :", save_path)
