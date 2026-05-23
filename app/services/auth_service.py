from flask_jwt_extended import create_access_token, create_refresh_token
from app.models.user import User
from app.utils.security import verify_password

def authenticate_user(email:str, password:str):
    user = User.query.filter_by(email=email).first()
    if not user:
        raise ValueError("Invalid credentials")
    
    is_valid_password = verify_password(password, user.password_hash)

    if not is_valid_password: 
        raise ValueError("Invalid credentials")
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    return {"access_token": access_token,"refresh_tokn": refresh_token, "user": {"id": user.id, "email": user.email}}