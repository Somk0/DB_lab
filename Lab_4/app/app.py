
from flask import Flask
from app.db.database import db

from app.controllers.buses_controller import buses_bp
from app.controllers.routes_controller import routes_bp
from app.controllers.drivers_controller import drivers_bp
from app.controllers.passengers_controller import passengers_bp
from app.controllers.assignments_controller import assignments_bp
from app.controllers.stops_controller import stops_bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@127.0.0.1:3306/Flixbus"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(buses_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(drivers_bp)
    app.register_blueprint(passengers_bp)
    app.register_blueprint(assignments_bp)
    app.register_blueprint(stops_bp)

    @app.route("/")
    def index():
        return "Flixbus API is running"

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


