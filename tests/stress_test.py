import requests
from image_encoder.image_encoder import encode
import time
import json
import os

endpoint1 = "http://localhost:5000/"
endpoint2 = "http://localhost:5001/get/"

files = os.listdir('sample_images/')

i = 0
start = time.time()
for file in files:
    if i > 30:
        break
    if not file == '.DS_Store':
        fname = 'sample_images/' + file

        r = requests.post(endpoint1,json={"fname":fname,"image":encode(fname)})
        print(r.text)
    i+=1


r = requests.get(endpoint2+'1')
print(r.text)
# res = json.loads(r.text)
end = time.time()

# for k,v in res.items():
#     for data in v:
#         if not "image" in data.keys():
#             print(data)


print("TOTAL TIME: {}".format(end-start))
