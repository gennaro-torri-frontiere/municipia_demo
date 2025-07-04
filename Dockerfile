FROM python:3.12

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    tesseract-ocr 
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt
