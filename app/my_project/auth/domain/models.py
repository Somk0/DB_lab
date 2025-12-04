from .db import db


class BusType(db.Model):
    __tablename__ = "bus_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    buses = db.relationship("Bus", back_populates="bus_type")

    def __repr__(self):
        return f"<BusType {self.id} {self.name}>"
    

class Bus(db.Model):
    __tablename__ = "buses"

    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(20), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    bus_type_id = db.Column(db.Integer, db.ForeignKey("bus_types.id"), nullable=False)
    bus_type = db.relationship("BusType", back_populates="buses")

    def __repr__(self):
        return f"<Bus {self.id} {self.plate_number}>"
    

class Route(db.Model):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    from_city = db.Column(db.String(50), nullable=False)
    to_city = db.Column(db.String(50), nullable=False)

    stops = db.relationship(
        "Stop",
        secondary="route_stops",
        back_populates="routes",
        order_by="RouteStop.sequence",
    )

    def __repr__(self):
        return f"<Route {self.id} {self.name}>"
    

class Stop(db.Model):
    __tablename__ = "stops"

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(50), nullable=False)

    routes = db.relationship(
        "Route",
        secondary="route_stops",
        back_populates="stops",
    )

    def __repr__(self):
        return f"<Stop {self.id} {self.city_name}>"
    

class RouteStop(db.Model):
    
    __tablename__ = "route_stops"

    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), primary_key=True)
    stop_id = db.Column(db.Integer, db.ForeignKey("stops.id"), primary_key=True)
    sequence = db.Column(db.Integer, nullable=False)  # номер зупинки у маршруті
