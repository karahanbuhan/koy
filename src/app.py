from flask import Flask, session, redirect, url_for
from routes.main import main_bp
from routes.serve import serve_bp

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("storage.log"), logging.StreamHandler()],
)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    app.secret_key = app.secret_key = app.config["SECRET_KEY"]

    # Save blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(serve_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
