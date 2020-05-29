from api import ModelPredictAPI
import json
import requests

def get_text(fpath):
    with open(fpath) as f:
        record = [json.loads(line) for line in f]
    text = record[0]["text"]
    return text


m = ModelPredictAPI()

def predict(fpath):
    text = get_text(fpath)
    input = {"text":[text]}

    output = m.post(input)
    print(output)
    to_send = {"fpath":fpath, "result":{"toxic_comment_results":str(output)}}
    requests.post('http://textdb:5000/append',json = to_send)

    return to_send



################ pika
if __name__ == "__main__":
    from pika_listener import QueueListener
    Q = QueueListener(predict, 'text_toxic')
    Q.run()


# powered by bee
