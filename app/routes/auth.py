from flask import request, jsonify
from app.routes import auth_bp
from app.services.auth_service import login_user, register_user, logout_user
from dotenv import load_dotenv

load_dotenv()

@auth_bp.route("/signup", methods=["POST"])
def register():
    data = request.get_json()
    return register_user(data)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = login_user(data)
    return result

@auth_bp.route("/logout", methods=["POST"])
def logout():
    data = request.get_json()
    result = logout_user(data)
    return jsonify(result)
