from flask import Flask
from flask_cors import CORS

from app.ui.utils import load_config
from app.my_project.auth.domain.db import db
from app.my_project.auth.route import register_blueprints


def create_app():
    cfg = load_config()

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = cfg["db"]["URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = cfg["flask"]["SECRET_KEY"]
    app.debug = cfg["flask"].get("DEBUG", False)

    CORS(app)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_blueprints(app)

    @app.get("/health")
    def health():
        return {"status": "OK"}, 200

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)
