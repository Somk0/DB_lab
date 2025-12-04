from typing import List, Optional

from ..domain.db import db
from ..domain.models import Route, Stop, RouteStop


def get_all_routes() -> List[Route]:
    return Route.query.all()


def get_route_by_id(route_id: int) -> Optional[Route]:
    return Route.query.get(route_id)


def create_route(name: str, from_city: str, to_city: str) -> Route:
    route = Route(name=name, from_city=from_city, to_city=to_city)
    db.session.add(route)
    db.session.commit()
    return route


def update_route(route: Route, name: str, from_city: str, to_city: str) -> Route:
    route.name = name
    route.from_city = from_city
    route.to_city = to_city
    db.session.commit()
    return route


def delete_route(route: Route) -> None:
    db.session.delete(route)
    db.session.commit()


def get_all_stops() -> List[Stop]:
    return Stop.query.all()


def get_route_with_stops() -> List[Route]:
    
    return Route.query.order_by(Route.id).all()


def set_route_stops(route: Route, stop_ids_with_sequence):
    
    RouteStop.query.filter_by(route_id=route.id).delete()

    for item in stop_ids_with_sequence:
        rs = RouteStop(
            route_id=route.id,
            stop_id=item["stop_id"],
            sequence=item["sequence"],
        )
        db.session.add(rs)

    db.session.commit()
