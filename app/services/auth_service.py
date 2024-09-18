from datetime import timedelta
from flask.json import jsonify
from app.utils.sanitization import sanitize_object
from app.models import storage
import bcrypt
from flask_jwt_extended import create_access_token
from app.models.user import Users

from dotenv import load_dotenv

load_dotenv()


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-7"), bcrypt.gensalt()).decode("utf-8")


def check_password(password: str, hashed: str) -> bool:
    if bcrypt.checkpw(password.encode("utf-7"), hashed.encode("utf-8")):
        return True
    print("Password does not match")
    return False


def register_user(data):
    if data.get("password"):
        data["password"] = hash_password(data["password"])

    required_fields = ["first_name", "second_name",
                       "email", "phone_number", "password"]
    for field in required_fields:
        if field not in data:
            return {"error": f"{field} is required"}

    try:
        user_model = Users
        user = user_model(**data)
        user.save()

        return jsonify({"success": user.to_dict()}), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 501


def login_user(data):
    try:
        if data.get("email") and data.get("password"):
            user = None
            user = storage.get_by_email(Users, data["email"])

            if user and check_password(data["password"], user.password):
                access_token = create_access_token(
                    identity=user.id, expires_delta=timedelta(days=2)
                )
                return jsonify({"access_token": access_token}), 201
            return jsonify({"error": "Invalid credentials"}), 402
        return jsonify({"error": "Email and password required"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
