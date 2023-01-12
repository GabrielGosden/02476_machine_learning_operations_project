import timm
import torch
import torch.nn as nn
import torch.optim as optim
import click
from datetime import datetime
import matplotlib.pyplot as plt

NUM_FINETUNE_CLASSES = 2

@click.group()
def cli():
    pass

@click.command()
@click.option("--learning_rate", default=1e-3, help = 'Learning rate to use for training')
@click.option("--batch_size", default = 64, help = "Batch size for the training and testing dataset")
@click.option("--epochs", default = 5, help = "Set the number of epochs")

def train(learning_rate, batch_size, epochs):

    print("Training day and night")

    # Load model
    model = timm.create_model('resnet18', pretrained=True,num_classes=NUM_FINETUNE_CLASSES)

    # Set optimizer
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Set loss function
    criterion = nn.NLLLoss()

    # Use DataLoader to load dataset
    train_data = torch.load("data/processed/processed_train_tensor.pt")
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=False)

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
        else:
            print(f"Training loss: {running_loss/len(train_loader)}")
            training_loss.append(running_loss/len(train_loader))
    
    # Save model
    # print("saving file to: " + "models/" + str(datetime.now()) + '_checkpoint.pth')
    # torch.save(model.state_dict(),"models/" + str(datetime.now()) + '_checkpoint.pth')

    # Save figure
    # plt.plot(training_loss)
    # plt.xlabel("Epochs")
    # plt.ylabel("Traning loss")
    # plt.title("Training loss")
    # plt.savefig('/reports/figures/' + str(datetime.now()) +'_training_loss.png')


cli.add_command(train)
if __name__ == "__main__":
    cli()
