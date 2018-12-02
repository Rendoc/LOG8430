FROM python:3-onbuild

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y mongodb

EXPOSE 5000

RUN service mongodb start

CMD ["python", "app.py"]
