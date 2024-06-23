import pika, json


params = pika.URLParameters('amqps://kxxkwlpk:5rd83BkFV2ln5F7gXCVVsCG927DZ41TN@puffin.rmq2.cloudamqp.com/kxxkwlpk')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    print('-------------------------==============================')
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='flask_b',
        body=json.dumps(body),
        properties=properties
    )

