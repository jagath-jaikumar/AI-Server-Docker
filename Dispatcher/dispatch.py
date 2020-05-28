from flask import Flask, request, make_response, jsonify
import requests

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def save_dispatch():
    packet = request.get_json()
    for k,v in packet.items():
        if k == "image":
            r = requests.post('http://imagedb:5000',json = packet)
            metadata_file = r.text

            

    return make_response(jsonify({"status":"queued", "file":r.text}), 200)




if __name__=="__main__":
    app.run(host='0.0.0.0')
