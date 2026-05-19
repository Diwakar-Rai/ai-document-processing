from app.extensions import db 
from app.models import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    documents = db.relationship("Document", backref="user", lazy = True)

    def __repr__(self):
        return f"<User {self.email}>"
    
from app.models.user import User
from app.models.document import Document