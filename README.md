02476 machine learning operations project
==============================

Project repository for 02476 machine learning operations

## How to build trainer docker image
```
docker build -f trainer.dockerfile . -t trainer:latest
```
## How to run trainer docker image
```
docker run --name <container_name> trainer:latest
```


02476 machine learning operations project description - Hot dog or not hot dog
------------

### Contributers 
Gabriel Gosden s174865 \
Mads Dudzik s174855 \
Tore Vang s183778\
Mate Andras s213734

### Overall goal of the project
The goal of the project is to use computer vision to solve a classification task of predicting whether a given image contains a hotdog or not.

### What framework are you going to use (Kornia, Transformer, Pytorch-Geometrics)
In this project we are going to use [PyTorch Image Models](https://github.com/rwightman/pytorch-image-models) (also known as TIMM) which is the absolutly most used computer vision package (maybe except for torchvision). It contains models, scripts and pre trained for a lot of state-of-the-art image models within computer vision.

### How to you intend to include the framework into your project
We are planning to use the pre-trained models of the TIMM framework to perform image classification. We are planning to use the CookieCutter file format for code structure. Git is going to be used for version control of the project. Github is the codebase for the project and DVC is going to be used for version control of the data. The group is planning to use Wandb for tracking and comparing training and evaluation runs. The group also want to include Hydra for variable handling and configuration. When the pipeline is developed the group wants to create a docker image suitable for a production setting.

### What data are you going to run on (initially, may change)

We are using the Kaggle dataset [Hot dog not hot dog](https://www.kaggle.com/datasets/dansbecker/hot-dog-not-hot-dog). The dataset is created from a subset of the [Food 101](https://www.kaggle.com/dansbecker/food-101) dataset. Our dataset contains a total of 1000 images. 500 contains hotdogs and 500 does not contain hotdogs.Images that do not contain hotdogs contains other types of food. The images are of variable size and the total dataset is ~100 mb.


### What deep learning models do you expect to use
We are planning to use a ResNet model for our image classfication. We are planning to use a lightweight version of ResNet, since the performance of the model is not important for this project. This will allow the group to focus on the pipeline instead of waiting for the model to train.


## Checklist
See [CHECKLIST.md](https://github.com/nielstiben/MLOPS-Project/blob/main/CHECKLIST.md)




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
