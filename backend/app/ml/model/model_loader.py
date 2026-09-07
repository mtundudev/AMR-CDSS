import torch
import timm,json
from pathlib import Path

MODEL_PATH = Path(__file__).with_name("model.pth")
CLASS_NAMES_PATH = Path(__file__).with_name("class_names.json")
with open(CLASS_NAMES_PATH, "r") as f:
    class_names = json.load(f)

model = timm.create_model(
	"tf_efficientnet_b0",
	pretrained=False,
	num_classes=20,
)
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu", weights_only=True))
model.eval()