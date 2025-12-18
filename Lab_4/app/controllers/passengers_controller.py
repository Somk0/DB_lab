
from flask import Blueprint, jsonify, request
from app.services.passengers_service import PassengerService

passengers_bp = Blueprint("passengers", __name__, url_prefix="/passengers")
service = PassengerService()

@passengers_bp.route("/", methods=["GET"])
def get_all():
    return jsonify([o.to_dict() for o in service.get_all()])

@passengers_bp.route("/<int:id>", methods=["GET"])
def get_one(id):
    obj = service.get_by_id(id)
    if not obj:
        return jsonify({"error": "Not found"}), 404
    return jsonify(obj.to_dict())

@passengers_bp.route("/", methods=["POST"])
def create():
    obj = service.create(request.json)
    return jsonify(obj.to_dict()), 201

@passengers_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    obj = service.update(id, request.json)
    if not obj:
        return jsonify({"error": "Not found"}), 404
    return jsonify(obj.to_dict())

@passengers_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    if not service.delete(id):
        return jsonify({"error": "Not found"}), 404
    return jsonify({"status": "deleted"})
