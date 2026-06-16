# models/employee.py

class Employee:
    def __init__(
        self,
        employee_id,
        name,
        email,
        department,
        salary,
        experience
    ):

        # validations (THIS FIXES YOUR FAIL)
        if salary <= 0:
            raise ValueError("Salary must be greater than 0")

        if "@" not in email:
            raise ValueError("Invalid email")

        if experience < 0:
            raise ValueError("Experience cannot be negative")

        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.experience = experience

    def calculate_bonus(self):
        if self.experience <= 2:
            bonus_percentage = 0.05
        elif self.experience <= 5:
            bonus_percentage = 0.10
        elif self.experience <= 10:
            bonus_percentage = 0.15
        else:
            bonus_percentage = 0.20

        return self.salary * bonus_percentage

    def update_details(self, name, email, department, salary, experience):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.experience = experience