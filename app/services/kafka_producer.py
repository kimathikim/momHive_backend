from confluent_kafka import Producer
import json
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


def send_user_message(sender_id, receiver_id, content):
    message_data = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "content": content,
        "timestamp": datetime.now().isoformat(),
    }

    producer.produce(
        "private_messages", key=str(sender_id), value=json.dumps(message_data)
    )
    producer.flush()


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
