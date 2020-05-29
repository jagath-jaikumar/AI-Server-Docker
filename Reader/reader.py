from flask import Flask
import json
import os


app = Flask(__name__)

@app.route("/get/<fname>", methods = ["GET"])
def get_data(fname):
    files = os.listdir('/var/lib/images/')
    data = {}
    record = []
    with open('/var/lib/images/' + fname + '.txt') as f:
        record = [str(line) for line in f]
    data[fname] = record
    return data


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001)
