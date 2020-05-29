FROM python:3.6

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY nude_detection.py pika_listener.py ./

CMD [ "python3", "-u","nude_detection.py" ]
