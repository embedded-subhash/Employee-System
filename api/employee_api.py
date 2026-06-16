employees = []

def get_employees():

    return {
        "status": 200,
        "data": employees
    }


def get_employee(employee_id):

    for emp in employees:

        if emp["id"] == employee_id:
            return {
                "status": 200,
                "data": emp
            }

    return {
        "status": 404,
        "message": "Employee not found"
    }


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
    }