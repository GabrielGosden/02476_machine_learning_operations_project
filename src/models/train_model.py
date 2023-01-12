from timm.data.dataset import ImageDataset
import timm

import torch
import torch.nn as nn
import torch.optim as optim
NUM_FINETUNE_CLASSES = 2

# Load train dataset
dataset = ImageDataset("./data/raw/train")
# image, label = dataset[0]
# print(image.size)
# print(len(dataset))


# Load model
model = timm.create_model('resnet18', pretrained=True,num_classes=NUM_FINETUNE_CLASSES)
model.eval()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.fc.parameters())
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def train_model(model, criterion, optimizer, num_epochs=3):
    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch+1, num_epochs))
        print('-' * 10)

        for phase in ['train', 'validation']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            running_corrects = 0

            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                outputs = model(inputs)
                loss = criterion(outputs, labels)

                if phase == 'train':
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()

                _, preds = torch.max(outputs, 1)
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / len(image_datasets[phase])
            epoch_acc = running_corrects.double() / len(image_datasets[phase])

            print('{} loss: {:.4f}, acc: {:.4f}'.format(phase,
                                                        epoch_loss,
                                                        epoch_acc))
    return model




model_trained = train_model(model, criterion, optimizer, num_epochs=3)