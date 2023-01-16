import click
import torch
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import torchvision
from torchvision import transforms

@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):

    transformsList = transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Resize((224,224)),
    ])

    trainPath = input_filepath+'/train/'
    trainDataset = torchvision.datasets.ImageFolder(
        root=trainPath,
        transform=transformsList
    ) 

    testPath = input_filepath+'/test/'
    testDataset = torchvision.datasets.ImageFolder(
        root=testPath,
        transform=transformsList
    )

    torch.save(trainDataset, output_filepath+'/processed_train_tensor.pt')
    torch.save(testDataset, output_filepath+'/processed_test_tensor.pt')

    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()