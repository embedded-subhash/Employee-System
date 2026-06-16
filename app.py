from flask import Flask, jsonify, request
from controllers import employee_controller
app = Flask(__name__)
app.register_blueprint(employee_bp)
@app.route("/")
def home():
    return {"messaage": "Mock REST API RUnning"}
# ---------------- MOCK DATABASE ----------------
employees = [
    {"id": 101, "name": "Subhash", "department": "Embedded", "salary": 50000},
    {"id": 102, "name": "Dhruv", "department": "Software", "salary": 60000},
    {"id": 103, "name": "Michael", "department": "IT", "salary": 55000}
]


# ---------------- HOME ----------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Employee JSON API Simulation Running"
    })


# ======================================================
# GET /employees  -> Get all employees
# ======================================================
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify({
        "count": len(employees),
        "employees": employees
    }), 200


# ======================================================
# GET /employees/{id} -> Get single employee
# ======================================================
@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return jsonify(emp), 200

    return jsonify({"error": "Employee not found"}), 404


# ======================================================
# POST /employees -> Create new employee
# ======================================================
@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    # basic validation
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    new_employee = {
        "id": data.get("id"),
        "name": data.get("name"),
        "department": data.get("department"),
        "salary": data.get("salary")
    }

    # check duplicate ID
    for emp in employees:
        if emp["id"] == new_employee["id"]:
            return jsonify({"error": "Employee ID already exists"}), 409

    employees.append(new_employee)

    return jsonify({
        "message": "Employee created successfully",
        "employee": new_employee
    }), 201


# ======================================================
# PUT /employees/{id} -> Update full employee
# ======================================================
@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = request.get_json()

    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = data.get("name")
            emp["department"] = data.get("department")
            emp["salary"] = data.get("salary")

            return jsonify({
                "message": "Employee updated successfully",
                "employee": emp
            }), 200

    return jsonify({"error": "Employee not found"}), 404


# ======================================================
# DELETE /employees/{id}
# ======================================================
@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)

            return jsonify({
                "message": "Employee deleted successfully"
            }), 200

    return jsonify({"error": "Employee not found"}), 404


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)