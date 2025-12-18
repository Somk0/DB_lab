
from app.db.database import db
from app.models.driver import Driver

class DriverDAO:
    def get_all(self):
        return Driver.query.all()

    def get_by_id(self, id):
        return Driver.query.get(id)

    def create(self, data):
        obj = Driver(**data)
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, id, data):
        obj = Driver.query.get(id)
        if not obj:
            return None
        for k, v in data.items():
            setattr(obj, k, v)
        db.session.commit()
        return obj

    def delete(self, id):
        obj = Driver.query.get(id)
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True
