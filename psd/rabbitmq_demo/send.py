#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('vwcm', 'vwcm')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '52.67.15.126', 5672, 'psd', credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
