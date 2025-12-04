from flask import Blueprint, jsonify, request

from ..service import route_service

route_bp = Blueprint("route_bp", __name__)


@route_bp.get("/routes")
def get_routes():
    data = route_service.get_all_routes()
    return jsonify(data), 200


@route_bp.get("/routes/<int:route_id>")
def get_route(route_id):
    try:
        data = route_service.get_route(route_id)
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@route_bp.post("/routes")
def create_route():
    try:
        payload = request.get_json() or {}
        data = route_service.create_route(payload)
        return jsonify(data), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@route_bp.put("/routes/<int:route_id>")
def update_route(route_id):
    try:
        payload = request.get_json() or {}
        data = route_service.update_route(route_id, payload)
        return jsonify(data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@route_bp.delete("/routes/<int:route_id>")
def delete_route(route_id):
    try:
        route_service.delete_route(route_id)
        return jsonify({"message": "Route deleted"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@route_bp.get("/stops")
def get_stops():
    
    data = route_service.get_all_stops()
    return jsonify(data), 200


@route_bp.get("/routes-with-stops")
def routes_with_stops():
   
    data = route_service.get_routes_with_stops()
    return jsonify(data), 200


@route_bp.post("/routes/<int:route_id>/stops")
def set_stops_for_route(route_id):
    
    try:
        payload = request.get_json() or []
        route_service.set_route_stops(route_id, payload)
        return jsonify({"message": "Stops updated for route"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
