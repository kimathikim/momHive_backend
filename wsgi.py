from app.utils.date_time import format_datetime
from app.models.groups import Groups
from app.models import storage
from app.factory import create_app
from app.extensions import redis_client, socketio
from flask_socketio import join_room
from flask import request
from uuid import uuid5
import json
import datetime

app = create_app()

# Configure SQLAlchemy to use QueuePool


class Messages:
    def __init__(self, id, sender_id, recipient_id, content, created_at):
        self.id = id
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.content = content
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": str(self.id),  # Convert UUID to string
            "sender_id": self.sender_id,
            "recipient_id": self.recipient_id,
            "content": self.content,
            "timestamp": self.created_at,
        }


@socketio.on("connect")
def handle_connect():
    print(f"Client connected: {request.sid}")
    return {"status": "connected"}


@socketio.on("disconnect")
def handle_disconnect():
    print(f"Client disconnected: {request.sid}")
    return {"status": "disconnected"}


def send_offline_messages(user_id, room):
    offline_messages = redis_client.lrange(f"offline_messages:{user_id}", 1, -1)
    print(f"Offline messages: {offline_messages}")

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


@socketio.on("join_private_room")
def join_private_room(data):
    sender_id = data.get("sender_id")
    receiver_id = data.get("receiver_id")

    if sender_id and receiver_id:
        room = f"private_{min(sender_id, receiver_id)}_{max(sender_id, receiver_id)}"
        join_room(room)
        # Notify the client that they joined the room successfully
        socketio.emit(
            "room_joined", {"status": "success", "room": room}, room=request.sid
        )
        print(f"User {sender_id} joined private room {room}")
    else:
        # Notify the client of the failure
        socketio.emit(
            "room_joined",
            {"status": "error", "message": "Invalid sender or receiver ID"},
            room=request.sid,
        )


# JOIN GROUP ROOM
@socketio.on("join_group_room")
def join_group_room(data):
    user_id = data.get("user_id")
    group_id = data.get("group_id")

    group = storage.get(Groups, group_id)
    if group and user_id in [member.user_id for member in group.members]:
        room = f"group_{group_id}"
        join_room(room)
        print(f"User {user_id} joined group room {room}")
    else:
        print(f"User {user_id} is not authorized to join group {group_id}")


@socketio.on("send_private_message")
def ws_send_private_message(data):
    sender_id = data.get("sender_id")
    receiver_id = data.get("receiver_id")
    content = data.get("content")

    if sender_id and receiver_id and content:
        room = f"private_{min(sender_id, receiver_id)}_{max(sender_id, receiver_id)}"

        message = Messages(
            id=uuid5(),
            sender_id=sender_id,
            recipient_id=receiver_id,
            content=content,
            created_at=datetime.datetime.now(),  # Ensure created_at is set
        )

        message_dict = message.to_dict()
        if message_dict["timestamp"]:
            message_dict["timestamp"] = format_datetime(message_dict["timestamp"])
        socketio.emit("receive_private_message", message_dict, room=room)
        print(f"Message sent successfully to private room: {room}")

        # Add the message to Redis for offline delivery
        # redis_client.rpush(f"offline_messages:{receiver_id}", json.dumps(message_dict))


@socketio.on("send_group_message")
def ws_send_group_message(data):
    sender_id = data.get("sender_id")
    group_id = data.get("group_id")
    content = data.get("content")

    group = storage.get(Groups, group_id)
    if group and sender_id in [member.user_id for member in group.members]:
        room = f"group_{group_id}"

        # Emit message to WebSocket room
        socketio.emit(
            "receive_group_message",
            {
                "sender_id": sender_id,
                "content": content,
                "timestamp": datetime.datetime.now().isoformat(),
            },
            room=room,
        )
        print(f"Group message sent to room {room}")
    else:
        print(f"Unauthorized message by user {sender_id} to group {group_id}")


application = app
