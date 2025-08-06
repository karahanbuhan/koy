import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DOMAIN = "https://karahanbuhan.com"

USERNAME = "admin"
PASSWORD = "sifre123"
SECRET_KEY = "çokgüçlübirkey"  # Flask session

MAX_UPLOAD_FOLDER_SIZE_GB = 5
UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp", "txt", "pdf", "zip"}

MAX_CONTENT_LENGTH = 2048 * 1024 * 1024  # 2GB

# Flask config
DEBUG = True
