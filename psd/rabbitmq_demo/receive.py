#/usr/bin/env python
import pika

<<<<<<< HEAD
credentials = pika.PlainCredentials('vwcm', 'vwcm')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '52.67.15.126', 5672, 'psd', credentials))
=======
credentials = pika.PlainCredentials('psd', 'psd')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'ec2-54-233-123-103.sa-east-1.compute.amazonaws.com', 5672, 'pratica_psd', credentials))
>>>>>>> 9e5c0b2628bc530ff3600da1c0e8191783db89b0
channel = connection.channel()


channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
