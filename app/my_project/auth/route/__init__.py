from flask import Flask

from ..controller.bus_controller import bus_bp
from ..controller.route_controller import route_bp


def register_blueprints(app: Flask):
    
    app.register_blueprint(bus_bp, url_prefix="/api")
    app.register_blueprint(route_bp, url_prefix="/api")
