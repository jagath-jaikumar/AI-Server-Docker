import requests
from image_encoder.image_encoder import encode
import time
endpoint1 = "http://localhost:5000/"
endpoint2 = "http://localhost:5000/get"


fname = "dog.jpg"

r = requests.post(endpoint1,json={"fname":fname,"image":encode(fname)})
print(r.text)


time.sleep(5)


r = requests.get(endpoint2)
print(r.text)
