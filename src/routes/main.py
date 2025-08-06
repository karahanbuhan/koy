from flask import Blueprint, request, redirect, url_for, session, render_template, flash
import config
import os
import uuid
from utils import get_storage_usage

main_bp = Blueprint("main", __name__)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in config.ALLOWED_EXTENSIONS
    )


@main_bp.route("/", methods=["GET", "POST"])
def index():
    uploaded_url = None

    if request.method == "POST":
        if not session.get("logged_in"):
            username = request.form.get("username")
            password = request.form.get("password")
            if username == config.USERNAME and password == config.PASSWORD:
                session["logged_in"] = True
                flash("Giriş başarılı", "success")
                return redirect(url_for("main.index"))
            else:
                flash("Hatalı giriş", "error")
        else:
            if "file" not in request.files or request.files["file"].filename == "":
                flash("Dosya seçilmedi", "error")
            else:
                file = request.files["file"]
                if allowed_file(file.filename):
                    ext = file.filename.rsplit(".", 1)[1].lower()
                    file.seek(0, os.SEEK_END)
                    file_size = file.tell()
                    file.seek(0)

                    used_gb, max_gb, _ = get_storage_usage()
                    total_after_upload = used_gb + (file_size / (1024 ** 3))

                    if total_after_upload > config.MAX_UPLOAD_FOLDER_SIZE_GB:
                        flash("Depolama alanı dolu! Yükleme iptal edildi.", "error")
                        return redirect(url_for("main.index"))

                    new_filename = f"{uuid.uuid4().hex}.{ext}"
                    save_path = os.path.join(config.UPLOAD_FOLDER, new_filename)
                    file.save(save_path)

                    if ext in {"png", "jpg", "jpeg", "gif", "webp"}:
                        path = url_for("serve.serve_image", filename=new_filename)
                    else:
                        path = url_for("serve.serve_file", filename=new_filename)

                    uploaded_url = f"{config.DOMAIN}{path}"

                else:
                    flash("Geçersiz dosya türü", "error")

    used_gb, max_gb, percent_used = get_storage_usage()

    return render_template(
        "index.html",
        logged_in=session.get("logged_in", False),
        uploaded_url=uploaded_url,
        used_gb=used_gb,
        max_gb=max_gb,
        percent_used=percent_used,
    )


@main_bp.route("/logout")
def logout():
    session.pop("logged_in", None)
    flash("Çıkış yapıldı", "info")
    return redirect(url_for("main.index"))
