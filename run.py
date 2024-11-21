from app.extensions import socketio
from app.factory import create_app

app = create_app()
jls_extract_var = __name__
if jls_extract_var == "__main__":
    app
