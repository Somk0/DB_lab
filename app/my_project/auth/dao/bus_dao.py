from typing import List, Optional

from ..domain.db import db
from ..domain.models import Bus, BusType


def get_all_buses() -> List[Bus]:
    return Bus.query.all()


def get_bus_by_id(bus_id: int) -> Optional[Bus]:
    return Bus.query.get(bus_id)


def create_bus(plate_number: str, capacity: int, bus_type_id: int) -> Bus:
    bus = Bus(plate_number=plate_number, capacity=capacity, bus_type_id=bus_type_id)
    db.session.add(bus)
    db.session.commit()
    return bus


def update_bus(bus: Bus, plate_number: str, capacity: int, bus_type_id: int) -> Bus:
    bus.plate_number = plate_number
    bus.capacity = capacity
    bus.bus_type_id = bus_type_id
    db.session.commit()
    return bus


def delete_bus(bus: Bus) -> None:
    db.session.delete(bus)
    db.session.commit()


def get_bus_types() -> List[BusType]:
    return BusType.query.all()


def get_buses_by_type(bus_type_id: int) -> List[Bus]:
    return Bus.query.filter_by(bus_type_id=bus_type_id).all()
