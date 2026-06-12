def validate_employee_id(employee_id):

    if employee_id <= 0:
        raise ValueError("Employee ID must be greater than 0.")

    return True


def validate_salary(salary):

    if salary < 0:
        raise ValueError("Salary cannot be negative.")

    return True


def validate_email(email):

    if "@" not in email:
        raise ValueError("Invalid email address.")

    return True