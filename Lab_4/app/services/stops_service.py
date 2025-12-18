from app.dao.stops_dao import StopsDAO

class StopsService:
    def __init__(self):
        self.dao = StopsDAO()

    def get_by_route(self, route_id):
        return self.dao.get_by_route(route_id)
