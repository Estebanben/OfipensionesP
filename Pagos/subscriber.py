import json
import pika
from sys import path
from os import environ
import django

# RabbitMQ connection settings
rabbit_host = '10.128.0.2'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'
exchange = 'pago_exchange'
topics = ['pago.#']

# Django setup
path.append('OfipensionesP/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'OfipensionesP.settings')
django.setup()

from Facturas.models import Factura
from Pagos.services.servicesPagos import send_email
from Pagos .models import Pago
from Pagos.logic.logicPagos import createPagoObject  # Import your createPagoObject function

# RabbitMQ connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))
channel = connection.channel()

channel.exchange_declare(exchange=exchange, exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
for topic in topics:
    channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=topic)

print('> Waiting for payments. To exit press CTRL+C')

# Callback function to handle the incoming messages
def callback(ch, method, properties, body):
    payload = json.loads(body.decode('utf8'))
    print(f"Received Payment: {payload}")

    # Extract payment details from the payload
    monto = payload['monto']
    tipo = payload['tipo']
    fecha = payload['fecha']
    factura_id = payload['factura_id']
    
    try:
    # Get the related factura object
       factura = Factura.objects.get(id=factura_id)

    # Use the createPagoObject function to create the Pago object
       createPagoObject(monto, tipo, fecha, None, factura)
    
    # Call the send_email function after creating the Pago
       send_email()

       print(f"Pago created successfully: {payload}")
    except Factura.DoesNotExist:
       print(f"Factura with id {factura_id} not found. Payment not created.")
    except Exception as e:
       print(f"Error creating payment: {e}")
       
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()