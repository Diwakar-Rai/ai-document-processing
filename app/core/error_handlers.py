import logging

from flask import jsonify


logger = logging.getLogger(__name__)


def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(error):
        logger.exception(str(error))

        return jsonify({
            "error": "Internal server error"
        }), 500