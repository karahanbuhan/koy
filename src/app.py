from flask import Flask
from routes.upload import upload_bp
from routes.serve import serve_bp


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Save blueprints
    app.register_blueprint(upload_bp)
    app.register_blueprint(serve_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
