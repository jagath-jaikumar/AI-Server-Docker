import requests
from image_encoder.image_encoder import encode

endpoint = "http://localhost:5000/"

fname = "dog.jpg"

r = requests.post(endpoint,json={"fname":fname,"image":encode(fname)})
print(r.text)
