import pika

def send(q, msg,host='localhost'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    channel.queue_declare(queue=q,durable=True)
    channel.basic_publish(exchange='',routing_key=q, body=msg)

    print(f'sent : {msg}')
    connection.close()

"""
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
"""
def listen(q, call_back,host='localhost'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    channel = connection.channel()

    channel.queue_declare(queue=q,durable=True)
    channel.basic_consume(queue =q, auto_ack=True, on_message_callback=call_back)
    print('waiting message...')
    channel.start_consuming()