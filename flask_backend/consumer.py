import pika, json


from main import Product, db



params = pika.URLParameters('amqps://kxxkwlpk:5rd83BkFV2ln5F7gXCVVsCG927DZ41TN@puffin.rmq2.cloudamqp.com/kxxkwlpk')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='flask_b')


def callback(ch, method, properties, body):
    print('Received in flask callback')
    # it is come from django app backend
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        print('qwerty ++++++____________++++++++++++')
        product = Product(
            id=data['id'],
            title=data['title'],
            price=data['price']
        )
        # this how to create object with SQLAlchemy
        db.session.add(product)
        db.session.commit()
        print('Product Created', product.id)

    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.price = data['price']
        db.session.commit()
        print('Product Updated', product.id)

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        if product:
            print('++++++++++++++', product.id)
            db.session.delete(product)
            db.session.commit()
            print('Product Deleted', product.id)
        else:
            print('++++++++++++++', product.id)
            print('Product Not Found')


channel.basic_consume(queue='flask_b', on_message_callback=callback, auto_ack=True)


print('Started consuming in flask backend')


channel.start_consuming()

channel.close()





