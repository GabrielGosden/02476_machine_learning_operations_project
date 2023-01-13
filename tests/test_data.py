#%%
import os.path
from pathlib import Path
import glob
import numpy as np
import timm
from pytest import mark
import torch

project_dir = str(Path(__file__).resolve().parents[1])
path = project_dir + "/data/processed/"

#load data
@mark.skipif(
    not os.path.exists(path), reason="Data files not found"
)  # skips datatest if file does not exist
def load_data():
    test = torch.load(path + 'processed_test_tensor.pt')
    train = torch.load(path + 'processed_train_tensor.pt')
    return test, train

test, train = load_data()

@mark.skipif(
    not os.path.exists(path), reason="Data files not found"
)  # skips datatest if file does not exist
def test_data():
    '''Run all tests related to data'''
    # test type
    assert str(type(test)) == "<class 'torchvision.datasets.folder.ImageFolder'>"
    assert str(type(train)) == "<class 'torchvision.datasets.folder.ImageFolder'>"

    # test shape
    assert str(test.transform) == 'Compose(\n    ToTensor()\n    Resize(size=(224, 224), interpolation=bilinear, max_size=None, antialias=None)\n)'
    assert str(train.transform) == 'Compose(\n    ToTensor()\n    Resize(size=(224, 224), interpolation=bilinear, max_size=None, antialias=None)\n)'
    
    return 

@mark.skipif(
    not os.path.exists(path), reason="Data files not found"
)  # skips datatest if file does not exist
def test_model():
    '''Run all tests related to the model'''
    # Load model
    model = timm.create_model('resnet18', pretrained=False, num_classes=2)
    last_model_name = glob.glob(project_dir + '/models/*')[-1]     
    state_dict = torch.load(last_model_name)
    model.load_state_dict(state_dict)
    # transfrom data
    test_loader = torch.utils.data.DataLoader(test, batch_size=32, shuffle=False)
    
    for images, labels in test_loader:
        ps = torch.exp(model(images.float()))
        print(ps)
        top_p, top_class = ps.topk(1, dim=1)
        # print(top_class,labels)
        equals = top_class == labels.view(*top_class.shape)
        accuracy = torch.mean(equals.type(torch.FloatTensor))
    accuracy = accuracy.item()*100

    # test accurary
    assert accuracy > 0.5

    return 
    
