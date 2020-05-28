FROM python:3

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 5000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY dispatch.py ./

CMD [ "python3", "-u","dispatch.py" ]
