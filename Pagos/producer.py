#!/usr/bin/env python
import time
import pika
from random import uniform,randint, choice
from datetime import datetime
import json

rabbit_host = '10.128.0.2'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'pago_exchange'
topic = 'pago.created'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

print('> Sending Pago information. To exit press CTRL+C')

# Simulating payment information
while True:
    monto = randint(1000, 5000)
    tipo = choice(['credit', 'debit', 'cash'])
    fecha = datetime.now().strftime('%Y-%m-%d')
    factura_id = randint(1, 10)  # Simulated factura ID
    
    # Create the payload
    payload = json.dumps({
        "monto": monto,
        "tipo": tipo,
        "fecha": fecha,
        "factura_id": 1
    })

    # Publish the message to the broker
    channel.basic_publish(exchange=exchange, routing_key=topic, body=payload)
    print(f"Payment created: {payload}")
    
    # Simulate delay
    time.sleep(5)

connection.close()