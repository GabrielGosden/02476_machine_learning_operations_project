# Base image
FROM python:3.9-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*
    # apt-get -y update; apt-get -y install curl


COPY requirements.txt requirements.txt
# COPY setup.py setup.py
COPY src/ src/
COPY reports/ reports/

# # Downloading gcloud package
# RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# # Installing the package
# RUN mkdir -p /usr/local/gcloud \
#   && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
#   && /usr/local/gcloud/google-cloud-sdk/install.sh

# # Adding the package path to local
# ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin
RUN mkdir –p /raw/test/hot_dog
RUN mkdir –p /raw/test/not_hot_dog
RUN mkdir –p /raw/train/not_hot_dog
RUN mkdir –p /raw/train/hot_dog
WORKDIR /   
RUN pip install -r requirements.txt --no-cache-dir


# # Copy data for training and testing
# RUN mkdir /data
# RUN gsutil -m cp -r gs://hotdogs2/* data


# CMD exec uvicorn train_model:app --port $PORT --host 0.0.0.0 --workers 1
# ENTRYPOINT ["streamlit", "run", "src/models/train_model.py", "--server.port=8501", "--server.address=0.0.0.0"]
ENTRYPOINT ["python", "-u", "/src/models/train_model.py","train"]
# CMD ["python", "-u", "${pwd}/src/models/train_model.py","train"]
# CMD exec 
