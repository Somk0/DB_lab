from dataclasses import asdict
from typing import List

from ..dao import route_dao
from ..domain.dto import RouteDTO, StopDTO, RouteWithStopsDTO
from ..domain.models import Route


def _route_to_dto(route: Route) -> RouteDTO:
    return RouteDTO(
        id=route.id,
        name=route.name,
        from_city=route.from_city,
        to_city=route.to_city,
    )


def get_all_routes():
    routes = route_dao.get_all_routes()
    return [asdict(_route_to_dto(r)) for r in routes]


def get_route(route_id: int):
    route = route_dao.get_route_by_id(route_id)
    if not route:
        raise ValueError("Route not found")
    return asdict(_route_to_dto(route))


def create_route(data: dict):
    name = data.get("name")
    from_city = data.get("from_city")
    to_city = data.get("to_city")

    if not all([name, from_city, to_city]):
        raise ValueError("Missing required fields")

    route = route_dao.create_route(name=name, from_city=from_city, to_city=to_city)
    return asdict(_route_to_dto(route))


def update_route(route_id: int, data: dict):
    route = route_dao.get_route_by_id(route_id)
    if not route:
        raise ValueError("Route not found")

    name = data.get("name", route.name)
    from_city = data.get("from_city", route.from_city)
    to_city = data.get("to_city", route.to_city)

    route = route_dao.update_route(
        route=route, name=name, from_city=from_city, to_city=to_city
    )
    return asdict(_route_to_dto(route))


def delete_route(route_id: int):
    route = route_dao.get_route_by_id(route_id)
    if not route:
        raise ValueError("Route not found")
    route_dao.delete_route(route)


def get_all_stops():
    stops = route_dao.get_all_stops()
    return [asdict(StopDTO(id=s.id, city_name=s.city_name)) for s in stops]


def get_routes_with_stops():
    """
    Вивід даних з M:M – для кожного маршруту перелік усіх його зупинок.
    """
    routes = route_dao.get_route_with_stops()
    result = []

    for r in routes:
        route_dto = _route_to_dto(r)
        stops_dto = [StopDTO(id=s.id, city_name=s.city_name) for s in r.stops]
        dto = RouteWithStopsDTO(route=route_dto, stops=stops_dto)
        result.append(asdict(dto))

    return result


def set_route_stops(route_id: int, items):
    """
    items – список об'єктів:
      [{"stop_id": 1, "sequence": 1}, {"stop_id": 3, "sequence": 2}, ...]
    """
    route = route_dao.get_route_by_id(route_id)
    if not route:
        raise ValueError("Route not found")

    if not isinstance(items, list) or not items:
        raise ValueError("Invalid stops format")

    route_dao.set_route_stops(route, items)
