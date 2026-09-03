from app.ml.model.model_loader import model
from io import BytesIO
from PIL import Image

def image_analysis(image_bytes:bytes):
    
    image=Image.open(BytesIO(image_bytes)).convert("RGB")
    
    results=model.predict(
        source=image,
        conf=0.25,
        save=False
    )
    predections=[]
    
    for result in results:
        for box in result.boxes:
            class_id=int(box.cls[0])
            confidence=float(box.conf[0])
            
            predections.append({
                "class_id":class_id,
                "class_name":result.names[class_id],
                "confidence":round(confidence,4)
                })
    return predections
