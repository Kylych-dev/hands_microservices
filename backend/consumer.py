import pika


params = pika.URLParameters('amqps://kxxkwlpk:5rd83BkFV2ln5F7gXCVVsCG927DZ41TN@puffin.rmq2.cloudamqp.com/kxxkwlpk')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='backend')


def callback(ch, method, properties, body):
    print('Received in admin callback')
    print(body, '-=-=-=-=-=-=-=-')


channel.basic_consume(queue='backend', on_message_callback=callback, auto_ack=True)


print('Started consuming in django app')


channel.start_consuming()

channel.close()


