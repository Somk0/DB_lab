from app.db.database import db

class Assignment(db.Model):
    __tablename__ = "Assignments"

    assignment_id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer)
    driver_id = db.Column(db.Integer)
    route_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            "assignment_id": self.assignment_id,
            "bus_id": self.bus_id,
            "driver_id": self.driver_id,
            "route_id": self.route_id
        }
