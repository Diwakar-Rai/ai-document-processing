import os 
from flask import current_app

from app.extensions import db 
from app.models.document import Document

from app.utils.file_utils import (allowed_file, generate_unique_filename)
from app.tasks.document_task import process_document_task

def save_documents(file, user_id):
    if file.filename == "":
        raise ValueError("No selected file")
    if not allowed_file(file.filename):
        raise ValueError("Invalid file type")
    original_filename = file.filename
    unique_filename = generate_unique_filename(original_filename)
    upload_folder = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, unique_filename)
    file.save(file_path)
    document = Document(filename = unique_filename, original_filename=original_filename, file_path=file_path, status='pending', user_id=user_id)

    db.session.add(document)
    db.session.commit()
    process_document_task.delay(document.id)
    return document