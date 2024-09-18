from flask import Blueprint, request, jsonify
from app.services.notification_service import save_notification
from app.services.kafka_producer import send_notification

notification_routes = Blueprint("notification_routes", __name__)


@notification_routes.route("/notifications", methods=["POST"])
def create_notification():
    """Create a new notification."""
    data = request.get_json()
    user_id = data.get("user_id")
    content = data.get("content")

    if not all([user_id, content]):
        return jsonify({"error": "Invalid data"}), 400

    notification = save_notification(user_id, content)
    # Send to Kafka for real-time processing
    send_notification(user_id, content)

    return jsonify(
        {
            "notification_id": notification.id,
            "timestamp": notification.timestamp.isoformat(),
        }
    ), 200


# @notification_routes.route("/notifications/<int:user_id>", methods=["GET"])
# def get_notifications(user_id):
#     """Retrieve notifications for a specific user."""
#     notifications = get_user_notifications(user_id)
#     return jsonify(
#         [
#             {
#                 "content": notification.content,
#                 "timestamp": notification.timestamp.isoformat(),
#             }
#             for notification in notifications
#         ]
#     ), 200
