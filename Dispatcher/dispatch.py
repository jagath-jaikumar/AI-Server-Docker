from flask import Flask, request, make_response, jsonify
import requests
import pika
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler




connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
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




@app.route("/get_images", methods = ["GET"])
def get_data_images():
    data = requests.get('http://imagedb:5000/get')
    return data.text


@app.route("/get_text", methods = ["GET"])
def get_data_text():
    data = requests.get('http://textdb:5000/get')
    return data.text



scheduler = BackgroundScheduler()
# scheduler.add_job(func=post_to_image_queue,args=['already queued'], trigger="interval", seconds=50)
# scheduler.add_job(func=post_to_text_queue,args=['already queued'], trigger="interval", seconds=50)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__=="__main__":
    app.run(host='0.0.0.0')


# powered by bee
