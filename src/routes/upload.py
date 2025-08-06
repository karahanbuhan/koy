import os
import uuid
from flask import Blueprint, request, redirect, render_template, current_app, flash, url_for
from werkzeug.utils import secure_filename

upload_bp = Blueprint("upload", __name__)


def allowed_file(filename):
    allowed = current_app.config["ALLOWED_EXTENSIONS"]
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed


@upload_bp.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("Dosya bulunamadı.")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("Dosya seçilmedi.")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            extension = filename.rsplit(".", 1)[1].lower()
            unique_name = f"{uuid.uuid4().hex}.{extension}"
            upload_path = os.path.join(current_app.config["UPLOAD_FOLDER"], unique_name)

            file.save(upload_path)

            if extension in {"png", "jpg", "jpeg", "gif", "webp"}:
                file_url = url_for(
                    "serve.serve_image", filename=unique_name, _external=True
                )
            else:
                file_url = url_for(
                    "serve.serve_file", filename=unique_name, _external=True
                )

            return f'Yüklendi: <a href="{file_url}" target="_blank">{file_url}</a>', 201

        else:
            flash("İzin verilmeyen dosya türü.")
            return redirect(request.url)

    return render_template("upload.html")
