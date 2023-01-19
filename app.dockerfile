FROM python:3.9

COPY requirements.txt /tmp/  
RUN pip install --upgrade pip  
RUN pip install torch --extra-index-url https://download.pytorch.org/whl/cpu  
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /src  
COPY src/ /src/  
RUN pip install -e /src

WORKDIR /

EXPOSE 80

CMD ["uvicorn", "src.app.fastapi_app:app", "--host", "0.0.0.0", "--port", "80"]