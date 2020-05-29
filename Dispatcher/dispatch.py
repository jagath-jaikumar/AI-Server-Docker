from flask import Flask, request, make_response, jsonify
import requests
import pika
import os
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', heartbeat=0))
channel = connection.channel()

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def save_dispatch():
    packet = request.get_json()
    for k,v in packet.items():
        if k == "image":
            metadata_file = requests.post('http://imagedb:5000',json = packet).text
            post_to_image_queue(metadata_file)
            return make_response(jsonify({"status":"queued", "file":metadata_file}), 200)

        if k == "text":
            metadata_file = requests.post('http://textdb:5000',json = packet).text
            post_to_text_queue(metadata_file)
            return make_response(jsonify({"status":"queued", "file":metadata_file}), 200)

    return make_response(jsonify({"status":"broken"}), 500)




def post_to_image_queue(body):
    channel.exchange_declare(exchange='fpaths',exchange_type='fanout')
    channel.basic_publish(exchange='fpaths', routing_key='ignored_for_fanout_exchanges', body=body)
    print(" [x] Sent {}".format(body))


def post_to_text_queue(body):
    channel.exchange_declare(exchange='textpaths',exchange_type='fanout')
    channel.basic_publish(exchange='textpaths', routing_key='ignored_for_fanout_exchanges2', body=body)
    print(" [x] Sent {}".format(body))





if __name__=="__main__":
    app.run(host='0.0.0.0')


# powered by bee
