import timm
import torch
import numpy as np
import click
import wandb

wandb.init(entity="mlopsproject",project="TheMLOpsProject")

NUM_FINETUNE_CLASSES = 2

@click.group()
def cli():
    pass

@click.command()
@click.argument("model_checkpoint")
@click.option("--batch_size", default = 4, help = "Batch size for the training and testing dataset")
def evaluate(model_checkpoint, batch_size):
    print("Evaluating until hitting the ceiling")

    config = wandb.config          # Initialize config
    config.batch_size = batch_size
    config.used_model_checkpoint = model_checkpoint

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
        
    found_accuracy = (np.mean(accuracy_total)/float(batch_size))*100
    print("acc: ",found_accuracy,"%")
    wandb.log({"Pediction Accuracy": found_accuracy})


cli.add_command(evaluate)


if __name__ == "__main__":
    cli()
