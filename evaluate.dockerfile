# Base image
FROM python:3.7-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*



COPY requirements.txt requirements.txt

WORKDIR /
RUN pip install -r requirements.txt --no-cache-dir
RUN dvc pull

COPY setup.py setup.py
COPY src/ src/
COPY data/ data/
COPY reports/ reports/
COPY models/ models/

ENTRYPOINT ["python", "-u", "src/models/predict_model.py","evaluate","2023-01-13 10:36:14.120301_checkpoint.pth"]
