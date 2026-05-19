from flask import Blueprint, request 
from app.services.user_service import create_user

users_bp = Blueprint("users", __name__, url_prefix='/users')

@users_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email and password are required"}, 400
    
    try:
        user = create_user(email=email, password_hash=password)
        return {"message": "User created Successfully", 'user': {"id": user.id, "email": user.email}}, 201
    except ValueError as e:
        return {"error": str(e)}, 400