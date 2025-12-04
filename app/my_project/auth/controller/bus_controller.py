from flask import Blueprint, jsonify, request

from ..service import bus_service

bus_bp = Blueprint("bus_bp", __name__)


@bus_bp.get("/buses")
def get_buses():
    
    data = bus_service.get_all_buses()
    return jsonify(data), 200


@bus_bp.get("/buses/<int:bus_id>")
def get_bus(bus_id):
    try:
        data = bus_service.get_bus(bus_id)
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@bus_bp.post("/buses")
def create_bus():
    
    try:
        payload = request.get_json() or {}
        data = bus_service.create_bus(payload)
        return jsonify(data), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@bus_bp.put("/buses/<int:bus_id>")
def update_bus(bus_id):
    
    try:
        payload = request.get_json() or {}
        data = bus_service.update_bus(bus_id, payload)
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@bus_bp.delete("/buses/<int:bus_id>")
def delete_bus(bus_id):
    
    try:
        bus_service.delete_bus(bus_id)
        return jsonify({"message": "Bus deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@bus_bp.get("/bus-types")
def get_bus_types():
    
    data = bus_service.get_bus_types()
    return jsonify(data), 200


@bus_bp.get("/bus-types/<int:type_id>/buses")
def get_buses_by_type(type_id):
    
    data = bus_service.get_buses_by_type(type_id)
    return jsonify(data), 200
