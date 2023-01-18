# Base image
FROM python:3.9-slim

ARG PORT=8080
EXPOSE $PORT

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/* &&\
    apt-get -y update; apt-get -y install curl


COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/
COPY reports/ reports/
# COPY .dvc/ .dvc/
# COPY .github/ .github/
# COPY data.dvc data.dvc
# COPY models.dvc models.dvc

# Downloading gcloud package
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# Installing the package
RUN mkdir -p /usr/local/gcloud \
  && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
  && /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

WORKDIR /   
RUN pip install -r requirements.txt --no-cache-dir
RUN mkdir /data
RUN gsutil -m cp -r gs://hotdogs2/* data

# RUN gcloud version
# RUN gcloud init --no-browser
# RUN gcloud auth application-default login --no-launch-browser
# RUN dvc pull

ENTRYPOINT ["python", "-u", "src/models/train_model.py","train"]