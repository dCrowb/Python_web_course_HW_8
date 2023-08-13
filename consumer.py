import pika
import time
from bson.objectid import ObjectId

from connect import mongo_db


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')



def stub():
    return True


def callback(ch, method, properties, body):
    message = body.decode()
    print(f" [x] Received {message}")
    time.sleep(1)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    send_message = stub()
    mongo_db.contact.update_one({"_id": ObjectId(message)}, {"$set": {"logic_field": True}})


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()