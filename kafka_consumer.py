import os
from confluent_kafka import Consumer, KafkaError
from app.extensions import socketio
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
        print(msg)

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

            if msg.topic() == PRIVATE_MESSAGES_TOPIC:
                room = f"private_{min(message['sender_id'], message['receiver_id'])}_{max(message['sender_id'], message['receiver_id'])}"
                print(f"Received private message: {message}")
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

            consumer.commit()
        except Exception as e:
            print(f"Error processing Kafka message: {str(e)}")


if __name__ == "__main__":
    print("Starting Kafka consumers")
    consume_messages()
#
# # Make sure to run the consumer in a background thread or separate process
# def start_kafka():
#     print("Starting Kafka consumers")
#     consumer_thread = threading.Thread(target=consume_messages)
#     consumer_thread.daemon = True
#     consumer_thread.start()
