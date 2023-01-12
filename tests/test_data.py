
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
    # data = load('/data/processed/')
    
    assert True
    return 

def test_model():
    '''Run all tests related to the model'''
    assert True
    return 