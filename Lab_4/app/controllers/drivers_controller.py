
from flask import Blueprint, jsonify, request
from app.services.drivers_service import DriverService

drivers_bp = Blueprint("drivers", __name__, url_prefix="/drivers")
service = DriverService()

@drivers_bp.route("/", methods=["GET"])
def get_all():
    return jsonify([o.to_dict() for o in service.get_all()])

@drivers_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    obj = service.get_by_id(id)
    if not obj:
        return jsonify({"error": "Not found"}), 404
    return jsonify(obj.to_dict())

@drivers_bp.route("/", methods=["POST"])
def create():
    obj = service.create(request.json)
    return jsonify(obj.to_dict()), 201

@drivers_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    obj = service.update(id, request.json)
    if not obj:
        return jsonify({"error": "Not found"}), 404
    return jsonify(obj.to_dict())

@drivers_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    if not service.delete(id):
        return jsonify({"error": "Not found"}), 404
    return jsonify({"status": "deleted"})
