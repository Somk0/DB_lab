from flask import Blueprint, jsonify
from app.services.assignments_service import AssignmentsService

assignments_bp = Blueprint("assignments", __name__, url_prefix="/assignments")
service = AssignmentsService()

@assignments_bp.get("/")
def get_assignments():
    data = service.get_all()
    return jsonify([a.to_dict() for a in data])
