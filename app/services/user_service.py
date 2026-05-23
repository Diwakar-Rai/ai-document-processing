from app.extensions import db
from app.models.user import User

from app.utils.security import hash_password

def create_user(email:str, password:str) -> User:
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        raise ValueError("User already exists")
    hashed_password = hash_password(password)
    user=User(email=email, password_hash=hashed_password)

    db.session.add(user)
    db.session.commit()

    return user