from app.db.database import db

class Stop(db.Model):
    __tablename__ = "Stops"

    stop_id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer)
    stop_name = db.Column(db.String(100))

    def to_dict(self):
        return {
            "stop_id": self.stop_id,
            "route_id": self.route_id,
            "stop_name": self.stop_name
        }
