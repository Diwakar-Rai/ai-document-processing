import time 
from app.extensions import db
from app.models.document import Document
from app.tasks.celery_app import celery
from app.utils.document_processing import (extract_text_from_image, extract_text_from_pdf)

@celery.task
def process_document_task(document_id):
    document = Document.query.get(document_id)
    if not document:
        return 
    try:
        document.status = "processing"
        db.session.commit()

        file_extension = (document.original_filename.rsplit(".", 1)[1].lower())
        extracted_text = ""

        if file_extension == 'pdf':
            extracted_text = extract_text_from_pdf(document.file_path)
        elif file_extension in ["png", 'jpg', "jpeg"]:
            extracted_text = extract_text_from_image(document.file_path)
        else:
            raise ValueError("Unsupported file type")
        document.extracted_text = extracted_text
        document.status = "completed"
        db.session.commit()
        
    except Exception:
        document.status = "failed"
        db.session.commit()
        raise