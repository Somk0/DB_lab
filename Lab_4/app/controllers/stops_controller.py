from flask import Blueprint, jsonify
from app.services.stops_service import StopsService

stops_bp = Blueprint("stops", __name__, url_prefix="/routes")
service = StopsService()

@stops_bp.get("/<int:route_id>/stops")
def get_stops_by_route(route_id):
    data = service.get_by_route(route_id)
    return jsonify([s.to_dict() for s in data])
