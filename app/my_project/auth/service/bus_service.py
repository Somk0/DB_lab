from dataclasses import asdict
from typing import List

from ..dao import bus_dao
from ..domain.dto import BusDTO
from ..domain.models import Bus


def _bus_to_dto(bus: Bus) -> BusDTO:
    return BusDTO(
        id=bus.id,
        plate_number=bus.plate_number,
        capacity=bus.capacity,
        bus_type=bus.bus_type.name if bus.bus_type else None,
    )


def get_all_buses():
    buses = bus_dao.get_all_buses()
    return [asdict(_bus_to_dto(b)) for b in buses]


def get_bus(bus_id: int):
    bus = bus_dao.get_bus_by_id(bus_id)
    if not bus:
        raise ValueError("Bus not found")
    return asdict(_bus_to_dto(bus))


def create_bus(data: dict):
    plate_number = data.get("plate_number")
    capacity = data.get("capacity")
    bus_type_id = data.get("bus_type_id")

    if not all([plate_number, capacity, bus_type_id]):
        raise ValueError("Missing required fields")

    bus = bus_dao.create_bus(
        plate_number=plate_number,
        capacity=int(capacity),
        bus_type_id=int(bus_type_id),
    )
    return asdict(_bus_to_dto(bus))


def update_bus(bus_id: int, data: dict):
    bus = bus_dao.get_bus_by_id(bus_id)
    if not bus:
        raise ValueError("Bus not found")

    plate_number = data.get("plate_number", bus.plate_number)
    capacity = data.get("capacity", bus.capacity)
    bus_type_id = data.get("bus_type_id", bus.bus_type_id)

    bus = bus_dao.update_bus(
        bus=bus,
        plate_number=plate_number,
        capacity=int(capacity),
        bus_type_id=int(bus_type_id),
    )
    return asdict(_bus_to_dto(bus))


def delete_bus(bus_id: int):
    bus = bus_dao.get_bus_by_id(bus_id)
    if not bus:
        raise ValueError("Bus not found")
    bus_dao.delete_bus(bus)


def get_bus_types():
    bus_types = bus_dao.get_bus_types()
    return [{"id": bt.id, "name": bt.name} for bt in bus_types]


def get_buses_by_type(bus_type_id: int):
    buses = bus_dao.get_buses_by_type(bus_type_id)
    return [asdict(_bus_to_dto(b)) for b in buses]
