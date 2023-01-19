import timm
import os
import wandb
import torch
import torch.nn as nn
import torch.optim as optim
import click
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
from google.cloud import storage


matplotlib.use('Agg')

# wandb.login(key="4b7e5e45520c218589c251e056eb7541ca081091")
# wandb.init(entity="mlopsproject",project="TheMLOpsProject")


NUM_FINETUNE_CLASSES = 2

@click.group()
def cli():
    pass


def save_model(name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('hotdogs2')
    blob = bucket.blob(name)
    blob.upload_from_filename(name)



def load_train_data():                                                                      
    # Instantiate a CGS client 
    client=storage.Client()
    bucket_name= "hotdogs2"

    # The "folder" where the files you want to download are
    folder="raw/"

    # Create this folder locally
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Retrieve all blobs with a prefix matching the folder
    bucket=client.get_bucket(bucket_name)
    blobs=list(bucket.list_blobs(prefix=folder))
    for blob in blobs:
        print(blob)
        if(not blob.name.endswith("/")):
            blob.download_to_filename("data/" + blob.name)
    
    train_file = open("data/processed/processed_train_tensor.pt", "wb")
    client.download_blob_to_file("gs://hotdogs2/processed/processed_train_tensor.pt", train_file)
    train_file.close()



@click.command()
@click.option("--learning_rate", default=1e-3, help = 'Learning rate to use for training')
@click.option("--batch_size", default = 32, help = "Batch size for the training and testing dataset")
@click.option("--epochs", default = 10, help = "Set the number of epochs")
@click.option("--model_arch", default = 'resnet18', help = "Model architecture available form TIMM")
@click.option("--optimizer_select", default = 'Adam', help = "Optimizer available from torch.optim")
def train(learning_rate, batch_size, epochs, model_arch, optimizer_select):

    print("Training day and night")

    # Load model
    model = timm.create_model(model_arch, pretrained=True,num_classes=NUM_FINETUNE_CLASSES)

    # Set optimizer
    if optimizer_select == 'Adam':
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    elif optimizer_select == 'SGD':
        optimizer = optim.SGD(model.parameters(), lr=learning_rate)


    # Set loss function
    criterion = nn.CrossEntropyLoss()

    # Use DataLoader to load dataset
    load_train_data()
    train_data = torch.load("processed/processed_train_tensor.pt")
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True)

    training_loss = []
    for e in range(epochs):
        running_loss = 0
        for images, labels in train_loader:
            optimizer.zero_grad()
            output = model(images.float())
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"Training loss: {running_loss/len(train_loader)}")
        # wandb.log({"Training loss": (running_loss/len(train_loader)),"Train Epoch Count": (e+1)})
        training_loss.append(running_loss/len(train_loader))
    
    # Save model

    timeStamp = str(datetime.now()).replace(" ","_")
    timeStamp = timeStamp.replace(".","_")
    timeStamp = timeStamp.replace(":","-")

    # wandb.log({"CheckpointID": (timeStamp + '_checkpoint.pth')})

    print("saving file to: " + timeStamp + '_checkpoint.pth')
    torch.save(model.state_dict(), timeStamp + '_checkpoint.pth')
    save_model(timeStamp + '_checkpoint.pth')

    # Save figure
    # plt.plot(training_loss)
    # plt.xlabel("Epochs")
    # plt.ylabel("Traning loss")
    # plt.title("Training loss")
    # plt.savefig('reports/figures/' + timeStamp +'_training_loss.png')
    
    # return "saving file to: " + "models/" + timeStamp + "_checkpoint.pth"


cli.add_command(train)
if __name__ == "__main__":
    cli()
