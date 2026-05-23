from flask import Blueprint, request 
from app.services.user_service import create_user
from app.services.auth_service import authenticate_user
from flask_jwt_extended import (jwt_required, get_jwt_identity)

users_bp = Blueprint("users", __name__, url_prefix='/users')

@users_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email and password are required"}, 400
    
    try:
        user = create_user(email=email, password=password)
        return {"message": "User created Successfully", 'user': {"id": user.id, "email": user.email}}, 201
    except ValueError as e:
        return {"error": str(e)}, 400
    
@users_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {
            "error": "Email and password are required"
        }, 400
    
    try:
        result =  authenticate_user(email, password)
        return result, 200
    except ValueError as e:
        return {"error": str(e)}, 401
    
@users_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    current_user_id = get_jwt_identity()

    return {"message": "Protected route accessed", "user_id": current_user_id}, 200