from flask import Flask, request, jsonify
from image_encoder.image_encoder import decode
import json
import os

app = Flask(__name__)
saved = []

counter = 1

@app.route("/", methods = ["POST"])
def save_data():
    global counter
    data = request.get_json()
    fname = data["fname"]

    if not fname in saved:
        metadata_file = '/var/lib/text/' + str(counter) + ".txt"
        with open(metadata_file, 'w') as outfile:
            json.dump(data, outfile)
            outfile.write(os.linesep)

        saved.append(fname)
        counter+=1
        return metadata_file

    return "already queued"



@app.route("/append", methods = ["POST"])
def add_data():
    data = request.get_json()
    file = data["fpath"]
    content = data["result"]

    with open(file, 'a') as f:
        json.dump(content, f)
        f.write(os.linesep)

    return "data added"



@app.route("/get", methods = ["GET"])
def get_data():
    files = os.listdir('/var/lib/text/')
    data = {}
    for filename in files:
        record = []
        with open('/var/lib/text/' + filename) as f:
            record = [json.loads(line) for line in f]
        data[filename] = record
    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0')


# powered by bee
