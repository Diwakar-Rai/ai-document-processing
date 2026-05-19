from app.extensions import db
from app.models.user import User

def create_user(email:str, password_hash:str) -> User:
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        raise ValueError("User already exists")
    user=User(email=email, password_hash=password_hash)

    db.session.add(user)
    db.session.commit()

    return user