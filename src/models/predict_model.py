import timm
import torch
import torch.nn as nn
import torch.optim as optim
import torchmetrics
import numpy as np
import click
from datetime import datetime


NUM_FINETUNE_CLASSES = 2

@click.group()
def cli():
    pass

@click.command()
@click.argument("model_checkpoint")
@click.option("--batch_size", default = 4, help = "Batch size for the training and testing dataset")

def evaluate(model_checkpoint, batch_size):
    print("Evaluating until hitting the ceiling")

    model = timm.create_model('resnet18', pretrained=False,num_classes=NUM_FINETUNE_CLASSES)
    state_dict = torch.load(model_checkpoint)
    model.load_state_dict(state_dict)

    test_data = torch.load("data/processed/processed_test_tensor.pt")
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=True)

    accuracy_total = []
    train_acc = 0
    for images, labels in test_loader:
        ps = torch.exp(model(images.float()))
        top_p, top_class = ps.topk(1, dim=1)
        top_class = torch.transpose(top_class,0,1)
        train_acc = torch.sum(top_class == labels)
        accuracy_total.append(train_acc)
    print("acc: ",(np.mean(accuracy_total)/float(batch_size))*100,"%")


cli.add_command(evaluate)


if __name__ == "__main__":
    cli()
