
from app.db.database import db

class Passenger(db.Model):
    __tablename__ = "Passengers"

    passenger_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))

    def to_dict(self):
        return {
            "passenger_id": self.passenger_id,
            "full_name": self.full_name,
            "phone": self.phone
        }
