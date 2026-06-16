# services/employee_service.py

from models.employee import Employee

# in-memory storage
_employees = {}


def reset_employees():
    """Clear all employees (used only for testing)"""
    global _employees
    _employees = {}


def add_employee(emp: Employee):
    if emp.employee_id in _employees:
        return False
    _employees[emp.employee_id] = emp
    return True


def get_all_employees():
    return list(_employees.values())


def get_employee_count():
    return len(_employees)


def get_average_salary():
    if not _employees:
        return 0
    total = sum(emp.salary for emp in _employees.values())
    return total / len(_employees)


def get_employee_bonus(emp_id):
    emp = _employees.get(emp_id)
    if not emp:
        return None
    return emp.calculate_bonus()


def get_total_salary(emp_id):
    emp = _employees.get(emp_id)
    if not emp:
        return None
    return emp.salary + emp.calculate_bonus()


def delete_employee(emp_id):
    return _employees.pop(emp_id, None)