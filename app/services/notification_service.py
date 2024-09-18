from app.models.notifications import Notifications
from app.services.kafka_producer import send_notification


def save_notification(user_id, content):
    """Save a notification to the database."""
    notification = Notifications(user_id=user_id, content=content)
    notification.save()
    return notification


# def get_user_notifications(user_id):
#     """Retrieve notifications for a specific user."""
#     return (
#         Notification.query.filter_by(user_id=user_id)
#         .order_by(Notification.timestamp.desc())
#         .all()
#     )
#
#
def handle_incoming_notification(data):
    """Process an incoming notification from Kafka."""
    user_id = data.get("user_id")
    content = data.get("content")

    save_notification(user_id, content)
    # Optionally send back to WebSocket or other systems
    send_notification(user_id, content)
