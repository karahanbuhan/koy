import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

USERNAME = os.getenv("KOY_USERNAME", "admin")
PASSWORD = os.getenv("KOY_PASSWORD", "sifre123")
SECRET_KEY = os.getenv("KOY_SECRET_KEY", "cokgizlisir")

DOMAIN = os.getenv("KOY_DOMAIN", "https://karahanbuhan.com")

MAX_UPLOAD_FOLDER_SIZE_GB = float(os.getenv("KOY_MAX_STORAGE_GB", "5"))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "..", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp", "txt", "pdf", "zip"}

MAX_CONTENT_LENGTH = 2048 * 1024 * 1024  # 2 GB limit (Flask için)
DEBUG = os.getenv("KOY_DEBUG", "false").lower() == "true"
