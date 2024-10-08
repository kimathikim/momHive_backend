from flask import Blueprint

auth_bp = Blueprint("/auth", __name__)
mentor_bp = Blueprint("/mentor", __name__)
events_bp = Blueprint("/event", __name__)
messages_bp = Blueprint("/message", __name__)
articles_bp = Blueprint("/article", __name__)
group_bp = Blueprint("/group", __name__)


def register_routes(app):
    app.register_blueprint(mentor_bp, url_prefix="/api/v1")
    app.register_blueprint(auth_bp, url_prefix="/api/v1")
    app.register_blueprint(messages_bp, url_prefix="/api/v1")
    app.register_blueprint(events_bp, url_prefix="/api/v1")
    app.register_blueprint(articles_bp, url_prefix="/api/v1")
    app.register_blueprint(group_bp, url_prefix="/api/v1")
