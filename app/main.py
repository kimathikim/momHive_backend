from app.factory import create_app
from app.extensions import socketio

app = create_app()


@socketio.on("send_message")
def handle_send_message(data):
    conversation_id = data["conversation_id"]

    emit("receive_message", data, room=conversation_id)


@socketio.on("join")
def handle_join(data):
    user_id = data["conversation_id"]
    join_room(user_id)

    emit(
        "user_joined", {"message": f"User {user_id} has joined the room"}, room=user_id
    )


if __name__ == "__main__":
    socketio.run(app, debug=True)
