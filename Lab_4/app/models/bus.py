
from app.db.database import db

class Bus(db.Model):
    __tablename__ = "Buses"

    bus_id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, nullable=False)
    manufacturer_id = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    mileage = db.Column(db.Integer)

    def to_dict(self):
        return {
            "bus_id": self.bus_id,
            "type_id": self.type_id,
            "manufacturer_id": self.manufacturer_id,
            "age": self.age,
            "capacity": self.capacity,
            "mileage": self.mileage
        }
