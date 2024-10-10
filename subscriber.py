import json
import pika
import time  # Import time to measure duration
from sys import path
from os import environ
import django
import signal  # To handle CTRL+C
import sys  # To handle system exit

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
from Pagos.models import Pago
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

# Variables to track time and count
total_time = 0
message_count = 0

def callback(ch, method, properties, body):
    global total_time, message_count
    
    payload = json.loads(body.decode('utf8'))
    print(f"Received Payment: {payload}")

    # Extract payment details from the payload
    monto = payload['monto']
    tipo = payload['tipo']
    fecha = payload['fecha']
    factura_id = payload['factura_id']
    
    try:
# Start timing
        start_time = time.time()

        # Get the related factura object
        factura = Factura.objects.get(id=factura_id)

        # Use the createPagoObject function to create the Pago object
        createPagoObject(monto, tipo, fecha, None, factura)

        # Call the send_email function after creating the Pago
        send_email()

        # End timing
        end_time = time.time()
        duration = end_time - start_time
        total_time += duration
        message_count += 1

        print(f"Pago created successfully: {payload} (Processing time: {duration:.4f} seconds)")

    except Factura.DoesNotExist:
        print(f"Factura with id {factura_id} not found. Payment not created.")
    except Exception as e:
        print(f"Error creating payment: {e}")
        
def print_average_time():
    if message_count > 0:
        avg_time = total_time / message_count
        print(f"\nProcessed {message_count} payments.")
        print(f"Average processing time: {avg_time:.4f} seconds")
    else:
        print("\nNo payments were processed.")

# Signal handler for CTRL+C
def signal_handler(sig, frame):
    print("\nCTRL+C detected! Exiting gracefully...")
    print_average_time()
    connection.close()  # Close the RabbitMQ connection
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()