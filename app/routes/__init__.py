from flask import Blueprint

auth_bp = Blueprint("/auth", __name__)
mentor_bp = Blueprint("/mentor", __name__)
event_bp = Blueprint("/event", __name__)
messages_bp = Blueprint("/message", __name__)
article_bp = Blueprint("/article", __name__)
group_bp = Blueprint("/group", __name__)


def register_routes(app):
    app.register_blueprint(mentor_bp, url_prefix="/api/v1")
    app.register_blueprint(auth_bp, url_prefix="/api/v1")
    app.register_blueprint(messages_bp, url_prefix="/api/v1")
    app.register_blueprint(event_bp, url_prefix="/api/v1")
    app.register_blueprint(article_bp, url_prefix="/api/v1")
    app.register_blueprint(group_bp, url_prefix="/api/v1")
