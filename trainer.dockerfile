# Base image
FROM python:3.7-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*



COPY requirements.txt requirements.txt
COPY setup.py setup.py
COPY src/ src/
COPY reports/ reports/
COPY .dvc/ .dvc/
COPY .github/ .github/
COPY data.dvc data.dvc
COPY models.dvc models.dvc



WORKDIR /
RUN pip install -r requirements.txt --no-cache-dir
RUN dvc remote add -d bikes gs://hotdogs
RUN dvc pull

ENTRYPOINT ["python", "-u", "src/models/train_model.py","train"]