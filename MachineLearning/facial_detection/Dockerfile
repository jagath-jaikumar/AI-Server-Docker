FROM python:3

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY haarcascade_frontalface_default.xml n_faces.py pika_listener.py ./

CMD [ "python3", "-u","n_faces.py" ]
