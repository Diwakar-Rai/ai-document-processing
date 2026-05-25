import os 
import uuid 
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}

def allowed_file(filename: str)->bool:
    return (
        "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

def generate_unique_filename(filename:str)-> str:
    extension = filename.rsplit(".", 1)[1].lower()
    unique_name = f"{uuid.uuid4()}.{extension}"
    return secure_filename(unique_name)