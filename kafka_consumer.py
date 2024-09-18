import os
from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Consumer, KafkaError, KafkaException
from flask_socketio import emit, join_room
from app.extensions import socketio
import threading
import json
from dotenv import load_dotenv

load_dotenv()
conf = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "PLAIN",
    "sasl.username": os.getenv("KAFKA_USER"),
    "sasl.password": os.getenv("KAFKA_PASSWORD"),
    "group.id": "message-consumer-group",
    "auto.offset.reset": "earliest",
}

# Kafka topics
PRIVATE_MESSAGES_TOPIC = "messages_topic"
GROUP_MESSAGES_TOPIC = "group_messages"

consumer = Consumer(conf)


def consume_messages():
    consumer.subscribe([PRIVATE_MESSAGES_TOPIC, GROUP_MESSAGES_TOPIC])

    while True:
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            continue  # No message retrieved
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue  # End of partition reached
            else:
                print(f"Kafka error: {msg.error()}")
                continue

        try:
            # Process the message
            message = json.loads(msg.value().decode("utf-8"))

            if msg.topic() == "private_messages":
                # Emit the private message to WebSocket room
                room = f"private_{min(message['sender_id'], message['receiver_id'])}_{max(message['sender_id'], message['receiver_id'])}"
                socketio.emit(
                    "receive_private_message",
                    {
                        "sender_id": message["sender_id"],
                        "content": message["content"],
                        "timestamp": message["timestamp"],
                    },
                    room=room,
                )
            elif msg.topic() == "group_messages":
                # Emit the group message to WebSocket room
                room = f"group_{message['group_id']}"
                socketio.emit(
                    "receive_group_message",
                    {
                        "sender_id": message["sender_id"],
                        "content": message["content"],
                        "timestamp": message["timestamp"],
                    },
                    room=room,
                )

            # Commit the message offset
            consumer.commit()

        except Exception as e:
            print(f"Error processing Kafka message: {str(e)}")


# Make sure to run the consumer in a background thread or separate process
def start_kafka():
    print("Starting Kafka consumers")
    consumer_thread = threading.Thread(target=consume_messages)
    consumer_thread.daemon = True
    consumer_thread.start()
