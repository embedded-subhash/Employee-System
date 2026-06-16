from flask import Blueprint, jsonify, request
from services import employee_service as service

employee_bp = Blueprint("employee_bp", __name__)


# GET ALL
@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    data = service.get_all()
    return jsonify({"count": len(data), "employees": data}), 200


# GET BY ID
@employee_bp.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    emp = service.get_by_id(emp_id)

    if emp:
        return jsonify(emp), 200

    return jsonify({"error": "Employee not found"}), 404


# CREATE
@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    result = service.create_employee(data)

    if result:
        return jsonify({"message": "Created", "employee": result}), 201

    return jsonify({"error": "Employee already exists"}), 409


# UPDATE
@employee_bp.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = request.get_json()

    result = service.update_employee(emp_id, data)

    if result:
        return jsonify({"message": "Updated", "employee": result}), 200

    return jsonify({"error": "Employee not found"}), 404


# DELETE
@employee_bp.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    result = service.delete_employee(emp_id)

    if result:
        return jsonify({"message": "Deleted"}), 200

    return jsonify({"error": "Employee not found"}), 404
