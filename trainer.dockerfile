# Base image
FROM python:3.9-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt
COPY src/ src/
COPY reports/ reports/

RUN mkdir /data
RUN mkdir /data/processed
RUN mkdir /data/raw
RUN mkdir /data/raw/test
RUN mkdir /data/raw/train
RUN mkdir /data/raw/test/not_hot_dog
RUN mkdir /data/raw/test/hot_dog
RUN mkdir /data/raw/train/not_hot_dog
RUN mkdir /data/raw/train/hot_dog

WORKDIR /   
RUN pip install -r requirements.txt --no-cache-dir


ENTRYPOINT ["python", "-u", "/src/models/train_model.py","train"]