import datetime
import json
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.routes import messages_bp
from app.models.messages import Messages
from app.models.groups import Groups
from app.extensions import socketio, redis_client
from app.services.kafka_producer import send_user_message, send_group_message
from app.services.rate_limiter import rate_limit
from app.models import storage


# PRIVATE MESSAGE ENDPOINT
@messages_bp.route("/messages/private", methods=["POST"])
@jwt_required()
@rate_limit(limit=10, per=60)  # 10 messages per minute
def send_private_message():
    user_id = get_jwt_identity()
    data = request.json

    # Input validation
    if not data or not all(k in data for k in ("receiver_id", "content")):
        return jsonify({"error": "Missing required fields"}), 400

    receiver_id = data["receiver_id"]
    content = data["content"]

    try:
        # Create and store message in DB
        message = Messages(sender_id=user_id, receiver_id=receiver_id, content=content)
        message.save()

        # Store in Redis for offline users
        room = f"private_{min(user_id, receiver_id)}_{max(user_id, receiver_id)}"
        redis_client.rpush(
            f"offline_messages:{receiver_id}",
            json.dumps(
                {
                    "sender_id": user_id,
                    "content": content,
                    "timestamp": message.timestamp.isoformat(),
                }
            ),
        )

        # Send to Kafka
        send_user_message(user_id, receiver_id, content)

        # Emit to WebSocket room
        socketio.emit(
            "receive_private_message",
            {
                "sender_id": user_id,
                "content": content,
                "timestamp": message.timestamp.isoformat(),
            },
            room=room,
        )

        return jsonify({"message": "Message sent successfully"}), 201

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Failed to send message"}), 500


# GROUP MESSAGE ENDPOINT
@messages_bp.route("/messages/group", methods=["POST"])
@jwt_required()
@rate_limit(limit=10, per=60)
def send_group_message_route():
    user_id = get_jwt_identity()
    data = request.json

    # Validate input
    if not data or not all(k in data for k in ("group_id", "content")):
        return jsonify({"error": "Missing required fields"}), 400

    group_id = data["group_id"]
    content = data["content"]

    # Ensure user is part of the group
    group = storage.get(Groups, group_id)
    if group and user_id in [member.id for member in group.members]:
        # Send message to Kafka
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
