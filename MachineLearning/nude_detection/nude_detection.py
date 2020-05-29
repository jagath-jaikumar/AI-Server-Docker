from image_encoder.image_encoder import decode
import json
import requests
from nudenet import NudeClassifier
import os

classifier = NudeClassifier()



def get_image(fpath):
    with open(fpath) as f:
        record = [json.loads(line) for line in f]
    img = decode(record[0]["image"])
    return img


def predict(fpath):
    img = get_image(fpath)
    img.save('temp.jpg')

    output = classifier.classify('temp.jpg')

    os.remove('temp.jpg')


    print(output)


    to_send = {"fpath":fpath, "result":{"nudenet_results":str(output)}}
    requests.post('http://imagedb:5000/append',json = to_send)


    return to_send





################ pika
if __name__ == "__main__":
    from pika_listener import QueueListener
    Q = QueueListener(predict, 'imageq_nude')
    Q.run()


# powered by bee
