from flask import Flask, request 
from app.config import Config 
from app.extensions import db, migrate, jwt 

from app.api.health.routes import health_bp
from app.api.users.routes import users_bp
from app.api.documents.routes import documents_bp
from app.core.logging_config import congigure_logging
from app.core.error_handlers import register_error_handlers
import logging

def create_app():
    congigure_logging()
    app=Flask(__name__)

    logger = logging.getLogger(__name__)
    register_error_handlers(app)
    @app.before_request
    def log_request_info():
        logger.info(f"{request.method}{request.path}")
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(documents_bp)
    
    return app