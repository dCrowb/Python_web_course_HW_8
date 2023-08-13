from faker import Faker
import pika
import json

import connect
from contact_model import Contact

COUNT_CONTACTS = 5

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.exchange_declare(exchange="task_mock", exchange_type="direct")
channel.queue_declare(queue="task_queue", durable=True)
channel.queue_bind(exchange="task_mock", queue="task_queue")


def seed():
    fake = Faker()
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
    ).save()
    return contact


def main():
    for _ in range(COUNT_CONTACTS):
        contact = seed()
        message = contact.id
        channel.basic_publish(
            exchange="task_mock",
            routing_key="task_queue",
            body=str(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print(" [x] Sent %r" % message)
    connection.close()


if __name__ == '__main__':
    main()