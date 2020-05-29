import requests
from image_encoder.image_encoder import encode
import time
import json


endpoint1 = "http://localhost:5000/"
endpoint2 = "http://localhost:5000/get"


fname = "dog.jpg"

r = requests.post(endpoint1,json={"fname":fname,"image":encode(fname)})
print(r.text)


time.sleep(5)


r = requests.get(endpoint2)
res = json.loads(r.text)


for k,v in res.items():
    for data in v:
        if not "image" in data.keys():
            print(data)
