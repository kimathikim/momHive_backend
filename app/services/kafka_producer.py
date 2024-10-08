from confluent_kafka import Producer
import json
from app.extensions import socketio
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

conf = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    "security.protocol": "SASL_SSL",
    "sasl.mechanism": "PLAIN",
    "sasl.username": os.getenv("KAFKA_USER"),
    "sasl.password": os.getenv("KAFKA_PASSWORD"),
}

producer = Producer(conf)


def send_user_message(sender_id, receiver_id, content, room):
    message_data = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "content": content,
        "timestamp": datetime.now().isoformat(),
    }

    producer.produce(
        "messages_topic", key=str(sender_id), value=json.dumps(message_data)
    )
    producer.flush()
    socketio.emit(
        "receive_private_message",
        {
            "sender_id": sender_id,
            "content": content,
            "timestamp": datetime.now().isoformat(),
        },
        room=room,
    )
    print(f"messafe sent successfully from kafka producer: {room}")


def send_group_message(sender_id, group_id, content):
    message_data = {
        "sender_id": sender_id,
        "group_id": group_id,
        "content": content,
        "timestamp": datetime.now().isoformat(),
    }

    producer.produce(
        "group_messages", key=str(group_id), value=json.dumps(message_data)
    )
    producer.flush()
