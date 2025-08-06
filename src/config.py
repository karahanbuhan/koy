import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp", "txt", "pdf", "zip"}

MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB

# Flask config
DEBUG = True
SECRET_KEY = "çokgizlianahtar"
