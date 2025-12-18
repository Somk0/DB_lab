
from flask import Blueprint, jsonify, request
from app.services.buses_service import BusService

buses_bp = Blueprint("buses", __name__, url_prefix="/buses")
service = BusService()

@buses_bp.route("/", methods=["GET"])
def get_all():
    return jsonify([o.to_dict() for o in service.get_all()])

@buses_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    obj = service.get_by_id(id)
    if not obj:
        return jsonify({"error": "Not found"}), 404
    return jsonify(obj.to_dict())

@buses_bp.route("/", methods=["POST"])
def create():
    obj = service.create(request.json)
    return jsonify(obj.to_dict()), 201

@buses_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    obj = service.update(id, request.json)
    if not obj:
        return jsonify({"error": "Not found"}), 404
    return jsonify(obj.to_dict())

@buses_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    if not service.delete(id):
        return jsonify({"error": "Not found"}), 404
    return jsonify({"status": "deleted"})
