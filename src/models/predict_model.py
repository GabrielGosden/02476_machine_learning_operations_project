import timm
import torch
import torch.nn as nn
import torch.optim as optim
import click
from datetime import datetime


NUM_FINETUNE_CLASSES = 2

@click.group()
def cli():
    pass



@click.command()
@click.argument("model_checkpoint")
@click.option("--batch_size", default = 64, help = "Batch size for the training and testing dataset")

def evaluate(model_checkpoint, batch_size):
    print("Evaluating until hitting the ceiling")

    model = timm.create_model('resnet18', pretrained=True,num_classes=NUM_FINETUNE_CLASSES)
    state_dict = torch.load(model_checkpoint)
    model.load_state_dict(state_dict)

    test_data = torch.load("/data/processed/processed_test_tensor.pt")
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False)

    for images, labels in test_loader:
        ps = torch.exp(model(images.float()))
        top_p, top_class = ps.topk(1, dim=1)
        equals = top_class == labels.view(*top_class.shape)
        accuracy = torch.mean(equals.type(torch.FloatTensor))

    print(f'Accuracy: {accuracy.item()*100}%')


cli.add_command(evaluate)


if __name__ == "__main__":
    cli()
