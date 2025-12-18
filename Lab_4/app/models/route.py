
from app.db.database import db

class Route(db.Model):
    __tablename__ = "Routes"

    route_id = db.Column(db.Integer, primary_key=True)
    start_point = db.Column(db.String(100))
    end_point = db.Column(db.String(100))
    total_distance = db.Column(db.Float)
    full_ticket_price = db.Column(db.Float)

    def to_dict(self):
        return {
            "route_id": self.route_id,
            "start_point": self.start_point,
            "end_point": self.end_point,
            "total_distance": self.total_distance,
            "full_ticket_price": self.full_ticket_price
        }
