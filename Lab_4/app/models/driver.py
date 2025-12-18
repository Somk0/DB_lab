
from app.db.database import db

class Driver(db.Model):
    __tablename__ = "Drivers"

    driver_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    license_number = db.Column(db.String(20), unique=True)
    experience_years = db.Column(db.Integer)

    def to_dict(self):
        return {
            "driver_id": self.driver_id,
            "full_name": self.full_name,
            "license_number": self.license_number,
            "experience_years": self.experience_years
        }
