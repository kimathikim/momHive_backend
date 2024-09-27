from flask import request
from app.routes import auth_bp
from app.services.auth_service import login_user, register_user
from flasgger import swag_from
from dotenv import load_dotenv

load_dotenv()


@auth_bp.route("/signup", methods=["POST"])
# @swag_from(
#     {
#         "tags": ["Registration"],
#         "description": "Register a new user",
#         "parameters": [
#             {
#                 "name": "data",
#                 "description": "Registration of the users",
#                 "in": "body",
#                 "required": False,
#                 "schema": swagger_schemas["Admins"],
#             }
#         ],
#         "responses": {
#             "201": {
#                 "description": "User registered successfully",
#                 "schema": {
#                     "type": "object",
#                     "properties": {
#                         "Admin": swagger_schemas["Admins"],
#                     },
#                 },
#             },
#             "400": {"description": "Bad request"},
#             "500": {"description": "Server error"},
#         },
#     }
# )
def register():
    data = request.get_json()
    return register_user(data)


@auth_bp.route("/login", methods=["POST"])
# @swag_from(
#     {
#         "tags": ["Authentication", "Pharmacy"],
#         "description": "Login to the system",
#         "parameters": [
#             {
#                 "name": "data",
#                 "description": "Login with your cridetials: email and password",
#                 "in": "body",
#                 "required": True,
#                 "schema": {
#                     "type": "object",
#                     "properties": {
#                         "email": {"type": "string", "format": "email"},
#                         "password": {"type": "string", "format": "password"},
#                     },
#                     "required": ["email", "password"],
#                 },
#             },
#         ],
#         "responses": {
#             "201": {
#                 "description": "Logged successfully",
#                 "schema": {
#                     "type": "object",
#                     "properties": {
#                         "access_token": {"type": "string"},
#                     },
#                 },
#             },
#             "400": {"description": "Bad request"},
#             "500": {"description": "Server error"},
#         },
#     }
# )
def login():
    data = request.get_json()
    result = login_user(data)
    return result
