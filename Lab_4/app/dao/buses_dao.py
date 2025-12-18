
from app.db.database import db
from app.models.bus import Bus

class BusDAO:
    def get_all(self):
        return Bus.query.all()

    def get_by_id(self, id):
        return Bus.query.get(id)

    def create(self, data):
        obj = Bus(**data)
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, id, data):
        obj = Bus.query.get(id)
        if not obj:
            return None
        for k, v in data.items():
            setattr(obj, k, v)
        db.session.commit()
        return obj

    def delete(self, id):
        obj = Bus.query.get(id)
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True
