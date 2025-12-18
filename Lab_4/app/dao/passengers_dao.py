
from app.db.database import db
from app.models.passenger import Passenger

class PassengerDAO:
    def get_all(self):
        return Passenger.query.all()

    def get_by_id(self, id):
        return Passenger.query.get(id)

    def create(self, data):
        obj = Passenger(**data)
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, id, data):
        obj = Passenger.query.get(id)
        if not obj:
            return None
        for k, v in data.items():
            setattr(obj, k, v)
        db.session.commit()
        return obj

    def delete(self, id):
        obj = Passenger.query.get(id)
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True
