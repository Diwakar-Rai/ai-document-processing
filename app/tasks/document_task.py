import time 
from app.extensions import db
from app.models.document import Document
from app.tasks.celery_app import celery

@celery.task
def process_document_task(document_id):
    document = Document.query.get(document_id)
    if not document:
        return 
    try:
        document.status = "processing"
        db.session.commit()
        time.sleep(10)
        document.extracted_text = (f"Processed content for document {document.id}")
        document.status = 'completed'
        db.session.commit()
    except Exception:
        document.status = "failed"
        db.session.commit()
        raise