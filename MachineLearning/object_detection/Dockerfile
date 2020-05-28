FROM python:3

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY imagenet_classes.txt object_detection.py pika_listener.py ./

ADD https://download.pytorch.org/models/alexnet-owt-4df8aa71.pth /root/.cache/torch/checkpoints/

CMD [ "python3", "-u","object_detection.py" ]
