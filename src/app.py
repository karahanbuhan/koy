import logging
from flask import Flask, session, redirect, url_for
from routes.main import main_bp
from routes.serve import serve_bp

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    app.secret_key = app.config["SECRET_KEY"]

    app.register_blueprint(main_bp)
    app.register_blueprint(serve_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
