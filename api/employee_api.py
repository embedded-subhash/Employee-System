<<<<<<< HEAD
employees = []

def get_employees():

    return {
        "status": 200,
=======
from models.employee import Employee
from services.employee_service import (
    add_employee,
    get_all_employees,
    delete_employee,
    get_employee_count,
    get_average_salary,
    get_employee_bonus,
    get_total_salary
)


def get_employees():

    employees = get_all_employees()

    return {
        "status": 200,
        "message": "Employees fetched successfully",
        "count": len(employees),
>>>>>>> 2be9917ca25795c557383cb97b5bb6cb36dba3da
        "data": employees
    }


<<<<<<< HEAD
def get_employee(employee_id):

    for emp in employees:

        if emp["id"] == employee_id:
            return {
                "status": 200,
                "data": emp
            }

=======
def create_employee(data):

    try:

        employee = Employee(
            data["employee_id"],
            data["name"],
            data["email"],
            data["department"],
            data["salary"],
            data["experience"]
        )

        if add_employee(employee):

            return {
                "status": 201,
                "message": "Employee created successfully"
            }

        return {
            "status": 400,
            "message": "Employee already exists"
        }

    except Exception as e:

        return {
            "status": 400,
            "message": str(e)
        }


def remove_employee(employee_id):

    employee = delete_employee(employee_id)

    if employee:

        return {
            "status": 200,
            "message": "Employee deleted successfully"
        }

>>>>>>> 2be9917ca25795c557383cb97b5bb6cb36dba3da
    return {
        "status": 404,
        "message": "Employee not found"
    }


<<<<<<< HEAD
def create_employee(employee):

    employees.append(employee)

    return {
        "status": 201,
        "message": "Employee created"
    }


def update_employee(employee_id, data):

    for emp in employees:

        if emp["id"] == employee_id:

            emp.update(data)

            return {
                "status": 200,
                "message": "Employee updated"
            }

    return {
        "status": 404,
        "message": "Employee not found"
    }


def delete_employee(employee_id):

    for emp in employees:

        if emp["id"] == employee_id:

            employees.remove(emp)

            return {
                "status": 200,
                "message": "Employee deleted"
            }

    return {
        "status": 404,
        "message": "Employee not found"
=======
def employee_report():

    return {
        "status": 200,
        "employee_count": get_employee_count(),
        "average_salary": get_average_salary()
    }


def employee_bonus(employee_id):

    bonus = get_employee_bonus(employee_id)

    if bonus is None:

        return {
            "status": 404,
            "message": "Employee not found"
        }

    return {
        "status": 200,
        "bonus": bonus
    }


def employee_total_salary(employee_id):

    total = get_total_salary(employee_id)

    if total is None:

        return {
            "status": 404,
            "message": "Employee not found"
        }

    return {
        "status": 200,
        "total_salary": total
>>>>>>> 2be9917ca25795c557383cb97b5bb6cb36dba3da
    }