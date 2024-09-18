# import datetime
# from logging import root
# from confluent_kafka import Producer
# import json
# from confluent_kafka import Consumer
# from flask_mail import Message
# from app.models.messages import Messages
# from app.models.conversation import Conversations
# from app.models import storage
# from flask import jsonify
# import app.services.kafka_producer as kafka_producer
# from app.extensions import socketio
#
# from flask_socketio import rooms
#
#
# def send_message(data):
#     sender_id = data.get("sender_id")
#     recipient_id = data.get("recipient_id")
#     content = data.get("content")
#     conversation_id = data.get("conversation_id")
#
#     if not sender_id or not recipient_id or not content or not conversation_id:
#         return {"error": "Missing required fields"}
#
#     new_message = Messages(
#         sender_id=sender_id,
#         recipient_id=recipient_id,
#         content=content,
#         conversation_id=conversation_id,
#     )
#     new_message.save()
#
#     kafka_data = {
#         "message_id": new_message.id,
#         "sender_id": sender_id,
#         "recipient_id": recipient_id,
#         "content": content,
#         "timestamp": new_message.timestamp.isoformat(),
#     }
#     kafka_producer.send_user_message("messages_topic", kafka_data)
#
#     socketio.emit("send_message", kafka_data, rooms(conversation_id))
#
#     return {"message": "Message sent successfully"}
#
#
# # Kafka configuration for the consumer
# kafka_conf = {
#     "bootstrap.servers": "pkc-4j8dq.southeastasia.azure.confluent.cloud:9092",
#     "security.protocol": "SASL_SSL",
#     "sasl.mechanism": "PLAIN",
#     "sasl.username": "C2T2XX7MRWRZCVGF",
#     "sasl.password": "TgSbpo0/r80QAplULOuj7MHR2ANiDjxWrjfDbwj7idjZ9I4AYkWwOyiQdVJoeI0Z",
#     "group.id": "message-consumer-group",
#     "auto.offset.reset": "earliest",
# }
# consumer = Consumer(kafka_conf)
#
#
# def get_messages(conversation_id):
#     consumer.subscribe(["messages_topic"])
#
#     messages = []
#     while True:
#         msg = consumer.poll(1.0)
#         if msg is None:
#             break
#         message_data = json.loads(msg.value().decode("utf-8"))
#
#         if message_data.get("conversation_id") == conversation_id:
#             messages.append(message_data)
#
#     return jsonify(messages), 200
#
#
# def list_conversations(user_id):
#     conversations = storage.get(Messages, user_id)
#     if not conversations:
#         return {"error": "No conversations found for this user"}, 404
#     conversations = [
#         {
#             "conversation_id": conversation.id,
#             "recipient_id": conversation.recipient_id,
#             "sender_id": conversation.sender_id,
#         }
#         for conversation in conversations
#     ]
#     return jsonify(conversations)
#
#
# def mark_messages_as_read(data):
#     message_ids = data.get("message_ids")
#     if not message_ids:
#         return {"error": "No message IDs provided"}
#
#     messages = storage.get(Messages, message_ids)
#     if not messages:
#         return {"error": "No messages found with provided message IDs"}, 404
#     for message in messages:
#         message.read = True
#         message.save()
#
#     return {"message": "Messages marked as read"}
#
#
# # Kafka Producer Configuration (same as before)
# producer = Producer(kafka_conf)
#
#
# def delete_message(message_id, user_id):
#     # Check if the user has permission to delete the message
#     message = storage.get(Messages, message_id)
#     if not message or message.sender_id != user_id:
#         return {"error": "Not authorized to delete this message"}, 403
#
#     storage.delete(message)
#
#     delete_event = {
#         "message_id": message_id,
#         "status": "deleted",
#         "timestamp": datetime.datetime.now().isoformat(),
#     }
#     producer.produce(
#         "message-deletions", value=json.dumps(delete_event).encode("utf-8")
#     )
#     producer.flush()
#
#     return {"message": "Message deleted successfully"}, 200
