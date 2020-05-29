import pika

class QueueListener:
    def __init__(self, predict_function, qn):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='rabbitmq', heartbeat=0))
        self.channel = connection.channel()

        self.channel.exchange_declare(exchange='textpaths', exchange_type='fanout')

        result = self.channel.queue_declare(queue=qn, exclusive=False)
        queue_name = result.method.queue

        self.channel.queue_bind(exchange='textpaths', queue=queue_name)

        print(' [*] Waiting for fpaths. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            fpath = body.decode("utf-8")
            print(" [x] Filepath: {}".format(fpath))
            if not fpath == "already queued":
                predict_function(fpath)


        self.channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)


    def run(self):
        self.channel.start_consuming()
