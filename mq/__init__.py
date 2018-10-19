import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('119.29.175.113', 5672, '/', credentials))
channel = connection.channel()
channel.exchange_declare(exchange="test-exe", exchange_type="direct",
                         passive=False, durable=True, auto_delete=False)
# 申明队列
channel.queue_declare(queue='balance')

def send_mq():
    msg = 'Hello, java lalalalaala '
    msg_prop = pika.BasicProperties()
    msg_prop.content_type = "text/plain"
    channel.basic_publish(exchange='test-exe', routing_key='balance', body=msg)
    print("send ·····")
    connection.close()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def customer_mq():
    channel.basic_consume(callback, queue='balance', no_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    send_mq()
    # customer_mq()



