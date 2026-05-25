from flask import Blueprint, request 
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from app.services.document_service import save_documents
documents_bp = Blueprint("documents", __name__, url_prfix="/documents")

@documents_bp.route("/upload", methods=["POST"])
@jwt_required()
def upload_document():
    if "file" not in request.files:
        return {"error": "No file part"}, 400
    file = request.files["file"]
    current_user_id = get_jwt_identity()
    try:
        document = save_documents(file=file,user_id=current_user_id)
        return {"message": "File uploaded successfully", "document": {"id": document.id, "filename": document.filename, "status": document.status}}, 201
    except ValueError as e:
        return {"error": str(e)}, 400