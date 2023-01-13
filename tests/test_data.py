#%%
import os.path
from pathlib import Path
import numpy as np
from pytest import mark

project_dir = str(Path(__file__).resolve().parents[1])
path = project_dir + "/data/processed/"


@mark.skipif(
    not os.path.exists(path), reason="Data files not found"
)  # skips datatest if file does not exist
def test_data():
    '''Run all tests related to data'''
    from torch import load

    # load data
    test = load(path + 'processed_test_tensor.pt')
    train = load(path + 'processed_train_tensor.pt')

    # test type
    assert str(type(test)) == "<class 'torchvision.datasets.folder.ImageFolder'>"
    assert str(type(train)) == "<class 'torchvision.datasets.folder.ImageFolder'>"

    # test shape
    assert str(test.transform) == 'Compose(\n    ToTensor()\n    Resize(size=(224, 224), interpolation=bilinear, max_size=None, antialias=None)\n)'
    assert str(train.transform) == 'Compose(\n    ToTensor()\n    Resize(size=(224, 224), interpolation=bilinear, max_size=None, antialias=None)\n)'
    
    return 

def test_model():
    '''Run all tests related to the model'''
    assert True
    return 
# %%
