FROM codait/max-base:v1.3.2
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

ARG model_bucket=https://max-cdn.cdn.appdomain.cloud/max-toxic-comment-classifier/1.0.0
ARG model_file=assets.tar.gz

WORKDIR /workspace

RUN wget -nv --show-progress --progress=bar:force:noscroll ${model_bucket}/${model_file} --output-document=assets/${model_file} && \
  tar -x -C assets/ -f assets/${model_file} -v && rm assets/${model_file}

COPY requirements.txt /workspace
RUN pip install -r requirements.txt

COPY . /workspace

EXPOSE 5000

CMD [ "python3", "-u","toxic_comments.py" ]
