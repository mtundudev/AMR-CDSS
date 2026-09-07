import torch
from io import BytesIO
from PIL import Image
from torchvision import transforms

from app.ml.model.model_loader import model,class_names


TRANSFORM = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=(0.485, 0.456, 0.406),
        std=(0.229, 0.224, 0.225),
    ),
])
def parse_class_name(raw_name: str):
    if "_gram stain" in raw_name:
        name = raw_name.replace("_gram stain", "").strip()
        return name, "gram_stain"
    elif "_media plate" in raw_name:
        name = raw_name.replace("_media plate", "").strip()
        return name, "media_plate"
    return raw_name.strip(), "unknown"

def image_analysis(image_bytes:bytes):
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    input_tensor = TRANSFORM(image).unsqueeze(0)

    with torch.inference_mode():
        probabilities = torch.softmax(model(input_tensor), dim=1)[0]

    top_probabilities, top_classes = torch.topk(probabilities, k=5)
    predictions = []
    for confidence, class_id in zip(top_probabilities, top_classes):
        class_index = int(class_id)
        name, specimen_type = parse_class_name(class_names[class_index])
        predictions.append({
            "class_id": class_index,
            "class_name": name,
            "specimen_type":specimen_type,
            "confidence": round(float(confidence), 4),
        })

    return predictions
