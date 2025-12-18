
from app.dao.drivers_dao import DriverDAO

class DriverService:
    def __init__(self):
        self.dao = DriverDAO()

    def get_all(self):
        return self.dao.get_all()

    def get_by_id(self, id):
        return self.dao.get_by_id(id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, id, data):
        return self.dao.update(id, data)

    def delete(self, id):
        return self.dao.delete(id)
