from app.models.stop import Stop

class StopsDAO:
    def get_by_route(self, route_id):
        return Stop.query.filter_by(route_id=route_id).all()
