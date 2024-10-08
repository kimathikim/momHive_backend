import datetime
import json
from app.models.messages import Messages
from flask import request
from app.utils.sanitization import sanitize_object
from flask_jwt_extended import decode_token
from flask_socketio import emit, join_room
from app.utils.date_time import format_datetime
from app.extensions import redis_client, socketio
from app.models import storage
from app.models.groups import Groups
from app.services.kafka_producer import send_group_message, send_user_message


@socketio.on("connect")
def handle_connect():
    token = request.args.get("token")
    if token:
        try:
            user_data = decode_token(token)
            user_id = user_data["sub"]
            print(f"User {user_id} connected")

        except Exception as e:
            print(f"Unauthorized WebSocket connection: {str(e)}")
            return False


def send_offline_messages(user_id, room):
    offline_messages = redis_client.lrange(
        f"offline_messages:{user_id}", 0, -1)
    print(f"offline messages: {offline_messages}")

    if offline_messages:
        for msg in offline_messages:
            try:
                msg = json.loads(msg)
                if msg["timestamp"]:
                    msg["timestamp"] = format_datetime(msg["timestamp"])
                socketio.emit("receive_private_message", msg, room=room)
            except TypeError as e:
                print(f"Error converting message to JSON: {str(e)}")
    redis_client.delete(f"offline_messages:{user_id}")


@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client disconnected: {request.sid}")


# JOIN PRIVATE ROOM
@socketio.on("join_private_room")
def join_private_room(data):
    token = data.get("token")
    receiver_id = data.get("receiver_id")

    try:
        user_data = decode_token(token)
        sender_id = user_data["sub"]

        room = f"private_{min(sender_id, receiver_id)}_{max(sender_id, receiver_id)}"
        join_room(room)
        send_offline_messages(sender_id, room)

        print(f"User {sender_id} joined private room {room}")

    except Exception:
        print("Failed to join private room")


# JOIN GROUP ROOM
@socketio.on("join_group_room")
def join_group_room(data):
    token = data.get("token")
    group_id = data.get("group_id")

    try:
        user_data = decode_token(token)
        user_id = user_data["sub"]

        # Ensure the user is part of the group
        group = storage.get(Groups, group_id)
        if group and user_id in [member.user_id for member in group.members]:
            room = f"group_{group_id}"
            join_room(room)
            print(f"User {user_id} joined group room {room}")
        else:
            print(
                f"Unauthorized attempt by {user_id} to join group {group_id}")

    except Exception:
        print("Failed to join group room")


@socketio.on("send_private_message")
def ws_send_private_message(data):
    token = data.get("token")
    content = data.get("content")
    receiver_id = data.get("receiver_id")

    try:
        user_data = decode_token(token)
        sender_id = user_data["sub"]
        room = f"private_{min(sender_id, receiver_id)}_{max(sender_id, receiver_id)}"

        message = Messages(
            sender_id=sender_id,
            recipient_id=receiver_id,
            content=content,
        )
        message.save()

        message = message.to_dict()
        if message["timestamp"]:
            message["timestamp"] = format_datetime(message["timestamp"])
        socketio.emit(
            "receive_private_message",
            message,
            room=room,
        )
        print(f"message sent successfully to private room: {room}")
        room = f"private_{min(sender_id, receiver_id)}_{max(sender_id, receiver_id)}"

        # Add the message to Redis
        redis_client.rpush(
            f"offline_messages:{receiver_id}", json.dumps(message))

    except Exception as e:
        print(f"Error sending private message: {str(e)}")


# SEND GROUP MESSAGE THROUGH WEBSOCKET
@socketio.on("send_group_message")
def ws_send_group_message(data):
    token = data.get("token")
    content = data.get("content")
    group_id = data.get("group_id")

    try:
        user_data = decode_token(token)
        sender_id = user_data["sub"]

        group = storage.get(Groups, group_id)
        if group and sender_id in [member.user_id for member in group.members]:
            room = f"group_{group_id}"
            #
            # # Send to Kafka for processing
            # send_group_message(sender_id, group_id, content)
            #
            # # Emit message to WebSocket room
            socketio.emit(
                "receive_group_message",
                {
                    "sender_id": sender_id,
                    "content": content,
                    "timestamp": datetime.datetime.now().isoformat(),
                },
                room=room,
            )

        else:
            print(
                f"Unauthorized message by user {sender_id} to group {group_id}")

    except Exception as e:
        print(f"Error sending group message: {str(e)}")
