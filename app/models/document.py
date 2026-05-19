from app.extensions import db 
from app.models import BaseModel

class Document(BaseModel):
    __tablename__ = "documents"
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")
    extracted_text = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Document {self.filename}>"