import requests
from image_encoder.image_encoder import encode
import time
import json
import os

endpoint1 = "http://localhost:5000/"
endpoint2 = "http://localhost:5001/get/"

files = os.listdir('sample_images/')
sent_files = []
i = 0



for file in files:
    if i > 30:
        break
    sent_files.append(file)
    if not file == '.DS_Store':
        fname = 'sample_images/' + file

        r = requests.post(endpoint1,json={"fname":file,"image":encode(fname)})
        print(r.text)
    i+=1

time.sleep(10)
for file in sent_files:
    r = requests.get(endpoint2+file)
    res = json.loads(r.text)
    for k,v in res.items():
        for data in v:
            if not "image" in data.keys():
                print(data)
