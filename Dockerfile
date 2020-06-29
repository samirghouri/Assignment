FROM python:3.7-alpine
RUN apk add --no-cache python3-dev \
    && pip install --upgrade pip
RUN apk add --update gcc libc-dev fortify-headers linux-headers && rm -rf /var/cache/apk/*
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
CMD ["python","app.py"]