
from app.db.database import db
from app.models.route import Route

class RouteDAO:
    def get_all(self):
        return Route.query.all()

    def get_by_id(self, id):
        return Route.query.get(id)

    def create(self, data):
        obj = Route(**data)
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, id, data):
        obj = Route.query.get(id)
        if not obj:
            return None
        for k, v in data.items():
            setattr(obj, k, v)
        db.session.commit()
        return obj

    def delete(self, id):
        obj = Route.query.get(id)
        if not obj:
            return False
        db.session.delete(obj)
        db.session.commit()
        return True
