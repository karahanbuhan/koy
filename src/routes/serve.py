import os
from flask import Blueprint, current_app, send_from_directory, abort
from utils import is_image

serve_bp = Blueprint("serve", __name__)


@serve_bp.route("/i/<path:filename>")
def serve_image(filename):
    if not is_image(filename):
        abort(404)
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)


@serve_bp.route("/f/<path:filename>")
def serve_file(filename):
    if is_image(filename):
        abort(404)
    return send_from_directory(
        current_app.config["UPLOAD_FOLDER"], filename, as_attachment=True
    )
