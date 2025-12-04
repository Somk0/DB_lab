from dataclasses import dataclass
from typing import List


@dataclass
class BusDTO:
    id: int
    plate_number: str
    capacity: int
    bus_type: str


@dataclass
class RouteDTO:
    id: int
    name: str
    from_city: str
    to_city: str


@dataclass
class StopDTO:
    id: int
    city_name: str


@dataclass
class RouteWithStopsDTO:
    route: RouteDTO
    stops: List[StopDTO]
