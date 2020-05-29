FROM python:3

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5001

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY reader.py ./

CMD [ "python3", "-u","reader.py" ]
