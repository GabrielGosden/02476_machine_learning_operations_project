# Base image
FROM python:3.9-slim

# install python
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*
    # apt-get -y update; apt-get -y install curl

COPY requirements_fastapi.txt requirements_fastapi.txt
# COPY setup.py setup.py
COPY src/ src/


EXPOSE 8080

WORKDIR /   
RUN pip install -r requirements_fastapi.txt --no-cache-dir

CMD ["uvicorn", "src.app.fastapi_app:app", "--host", "0.0.0.0", "--port", "8080"]