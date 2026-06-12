import json
from models.employee import Employee


class EmployeeManager:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):

        for emp in self.employees:
            if emp.employee_id == employee.employee_id:
                print("Employee ID already exists.")
                return

        self.employees.append(employee)
        print("Employee added successfully.")

    def view_employees(self):

        if not self.employees:
            print("No employees found.")
            return

        for employee in self.employees:
            employee.display_details()

    def search_employee(self, employee_id):

        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.display_details()
                return

        print("Employee not found.")

    def update_employee(self, employee_id, new_salary):

        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.salary = new_salary
                print("Employee salary updated successfully.")
                return

        print("Employee not found.")

    def delete_employee(self, employee_id):

        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print("Employee deleted successfully.")
                return

        print("Employee not found.")

    def save_data(self):

        employee_data = []

        for employee in self.employees:
            employee_data.append(employee.to_dict())

        with open("data/employees.json", "w") as file:
            json.dump(employee_data, file, indent=4)

        print("Employee data saved successfully.")

    def load_data(self):

        try:
            with open("data/employees.json", "r") as file:
                employee_data = json.load(file)

            self.employees = []

            for emp_dict in employee_data:

                employee = Employee(
                    emp_dict["employee_id"],
                    emp_dict["name"],
                    emp_dict["email"],
                    emp_dict["department"],
                    emp_dict["salary"],
                    emp_dict["experience"]
                )

                self.employees.append(employee)

            print("Employee data loaded successfully.")

        except FileNotFoundError:
            print("No existing employee data found.")

        except json.JSONDecodeError:
            print("employees.json is empty or invalid.")