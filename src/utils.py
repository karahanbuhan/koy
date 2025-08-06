import os
import config
from functools import wraps
from flask import session, redirect, url_for


def get_folder_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size


def is_image(filename):
    ext = filename.rsplit(".", 1)[-1].lower()
    return ext in {"png", "jpg", "jpeg", "gif", "webp"}


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login.login"))
        return f(*args, **kwargs)

    return decorated_function


def get_storage_usage():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(config.UPLOAD_FOLDER):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    used_gb = total_size / (1024**3)
    max_gb = config.MAX_UPLOAD_FOLDER_SIZE_GB
    percent_used = min(100, (used_gb / max_gb) * 100)
    return used_gb, max_gb, percent_used
