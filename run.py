from app.extensions import socketio
from app.factory import create_app
from kafka_consumer import start_kafka

app = create_app()
jls_extract_var = __name__
if jls_extract_var == "__main__":
    start_kafka()
    socketio.run(app, debug=True)
