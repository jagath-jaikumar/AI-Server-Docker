import cv2
import sys
import json
from image_encoder.image_encoder import decode
import numpy
import requests
# Get user supplied values

def get_image(fpath):
    with open(fpath) as f:
        record = [json.loads(line) for line in f]
    img = decode(record[0]["image"])
    return img


def n_faces(fpath):
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    img = get_image(fpath)

    image = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    output = {}
    i = 1
    for (x, y, w, h) in faces:
        k = "face"+str(i)
        output[k] = [int(x),int(y), int(x+w), int(y+h)]
        i+=1

    print(output)

    to_send = {"fpath":fpath, "result":{"faces":output}}
    requests.post('http://imagedb:5000/append',json = to_send)


    return to_send


if __name__ == "__main__":
    from pika_listener import QueueListener
    Q = QueueListener(n_faces, 'imageq_n_faces')
    Q.run()


# powered by bee
