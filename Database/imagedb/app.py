from flask import Flask, request
from image_encoder.image_encoder import decode
import json

app = Flask(__name__)
saved = []

counter = 1

@app.route("/", methods = ["POST"])
def save_data():
    global counter
    data = request.get_json()
    fname = data["fname"]

    if not fname in saved:
        metadata_file = '/var/lib/images/' + str(counter) + ".txt"
        with open(metadata_file, 'a') as outfile:
            json.dump(data, outfile)

        saved.append(fname)
        counter+=1


    return metadata_file


if __name__ == "__main__":
    app.run(host='0.0.0.0')
