import requests
from image_encoder.image_encoder import encode
import time
import json


endpoint1 = "http://localhost:5000/"
endpoint2 = "http://localhost:5001/get"


fname = "dog.jpg"

start = time.time()

r = requests.post(endpoint1,json={"fname":fname,"image":encode(fname)})

print(r.text)



r = requests.get(endpoint2)
res = json.loads(r.text)
end = time.time()

for k,v in res.items():
    for data in v:
        if not "image" in data.keys():
            print(data)


print("TOTAL TIME: {}".format(end-start))

# endpoint1 = "http://localhost:5000/"
# endpoint2 = "http://localhost:5000/get_text"
#
#
# fname = "sample_text"
# start = time.time()
# r = requests.post(endpoint1,json={"fname":fname,"text":"Hello World!"})
# print(r.text)
#
#
#
#
# r = requests.get(endpoint2)
# res = json.loads(r.text)
# end = time.time()
#
# for k,v in res.items():
#     for data in v:
#         if not "image" in data.keys():
#             print(data)
# print("TOTAL TIME: {}".format(end-start))
