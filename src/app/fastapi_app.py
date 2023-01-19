from fastapi import FastAPI, UploadFile, File
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import timm
import os
from PIL import Image
import glob
from google.cloud import storage
import io

storage_client = storage.Client()
checkpoint_load = open("local_checkpoint.pth", "wb")
storage_client.download_blob_to_file("gs://hotdogs2/models/checkpoint.pth", checkpoint_load)
checkpoint_load.close()


app = FastAPI()

# Load the pre-trained model from a checkpoint file
model = timm.create_model('resnet18', pretrained=True,num_classes=2)
# model_dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "models"))
# last_model_path = glob.glob(model_dir_path + '/checkpoints/*')[-1]
checkpoint = torch.load("local_checkpoint.pth")
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
    image = Image.open(io.BytesIO(image))
    # image = Image.open(image.file)
    image = preprocess_image(image)

# @app.post("/classify-image/")
# async def cv_model(data: UploadFile = File(...)):
#    with open('image.jpg', 'wb') as image:
#       content = await data.read()
#       image.write(content)
#       image.close()


    # Perform inference
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)

    # Return the result
    return {"class_id": predicted.item()}