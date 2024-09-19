import datetime
from app.utils.date_time import format_datetime
import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.routes import messages_bp
from app.models.messages import Messages
from app.models.groups import Groups
from app.models.user import Users
from app.extensions import socketio, redis_client
from app.services.kafka_producer import send_user_message, send_group_message
from app.services.rate_limiter import rate_limit
from app.models import storage


@messages_bp.route("/messages/users", methods=["GET"])
@jwt_required()
def get_users():
    user_id = get_jwt_identity()
    users = storage.all(Users)
    users = [user.to_dict() for user in users if user.id != user_id]
    return jsonify(users), 200


@messages_bp.route("/messages/private/<recipient_id>", methods=["GET"])
@jwt_required()
def get_private_messages(recipient_id):
    user_id = get_jwt_identity()

    messages = storage.all(Messages)

    messages = [
        message.to_dict()
        for message in messages
        if message.sender_id in [user_id, recipient_id]
        and message.recipient_id in [user_id, recipient_id]
    ]
    # Sort the messages by timestamp
    messages.sort(key=lambda x: x["timestamp"])
    return jsonify(messages), 200


@messages_bp.route("/messages/private", methods=["POST"])
@jwt_required()
@rate_limit(limit=10, per=60)
def send_private_message():
    sender_id = get_jwt_identity()
    print(sender_id)
    data = request.json

    if not data or not all(k in data for k in ("receiver_id", "content")):
        return jsonify({"error": "Missing required fields"}), 400

    recipient_id = data["receiver_id"]
    content = data["content"]

    try:
        message = Messages(
            sender_id=sender_id,
            recipient_id=recipient_id,
            content=content,
        )
        message.save()

        message = message.to_dict()
        if message["timestamp"]:
            message["timestamp"] = format_datetime(message["timestamp"])

        redis_client.rpush(
            f"offline_messages:{recipient_id}",
            json.dumps(
                message_data,
            ),
        )
        return jsonify({"message": "Message sent successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@messages_bp.route("/messages/contacts", methods=["GET"])
@jwt_required()
def get_mycont():
    user_id = get_jwt_identity()
    messages = storage.all(Messages)
    messages = [
        message.to_dict() for message in messages if message.sender_id == user_id
    ]
    recipients = []
    if messages:
        for message in messages:
            recipient = storage.get(Users, message["recipient_id"])
            if recipient:
                recipients.append(recipient.to_dict())

    return jsonify(recipients), 200


@messages_bp.route("/messages/group", methods=["POST"])
@jwt_required()
@rate_limit(limit=10, per=60)
def send_group_message_route():
    user_id = get_jwt_identity()
    data = request.json

    if not data or not all(k in data for k in ("group_id", "content")):
        return jsonify({"error": "Missing required fields"}), 400

    group_id = data["group_id"]
    content = data["content"]

    group = storage.get(Groups, group_id)
    if group and user_id in [member.id for member in group.members]:
        send_group_message(user_id, group_id, content)

        room = f"group_{group_id}"
        socketio.emit(
            "receive_group_message",
            {
                "sender_id": user_id,
                "content": content,
                "timestamp": datetime.datetime.now().isoformat(),
            },
            room=room,
        )
        return jsonify({"message": "Message sent"}), 200
    else:
        return jsonify({"error": "Unauthorized access to group"}), 403
