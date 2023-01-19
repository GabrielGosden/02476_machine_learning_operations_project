from fastapi import FastAPI, UploadFile
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import timm
import os
from PIL import Image

app = FastAPI()

# Load the pre-trained model from a checkpoint file
model = timm.create_model('resnet18', pretrained=True,num_classes=2)
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "models", "2023-01-19_10-42-10_810804_checkpoint.pth"))
checkpoint = torch.load(model_path)
model.load_state_dict(checkpoint)
model.eval()

@app.post("/classify-image/")
async def classify_image(file: UploadFile):
    
    # Define image preprocessing function
    def preprocess_image(image):
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize((224,224)),
        ])
        return transform(image).unsqueeze(0)

    # Read image file and preprocess
    image = await file.read()
    image = Image.open(image.file)
    image = preprocess_image(image)

    # Perform inference
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)

    # Return the result
    return {"class_id": predicted.item()}