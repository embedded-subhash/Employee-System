from services.employee_manager import EmployeeManager
from utils.helper import print_header, get_current_time

def main():

    print_header("EMPLOYEE MANAGEMENT SYSTEM")
    print("Current Time:", get_current_time())

    manager = EmployeeManager()

    # Load existing data first
    manager.load_data()

    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee Salary")
        print("5. Delete Employee")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            emp_id = int(input("ID: "))
            name = input("Name: ")
            email = input("Email: ")
            dept = input("Department: ")
            salary = float(input("Salary: "))
            exp = int(input("Experience: "))

            from models.employee import Employee
            emp = Employee(emp_id, name, email, dept, salary, exp)

            manager.add_employee(emp)

        elif choice == "2":
            manager.view_employees()

        elif choice == "3":
            emp_id = int(input("Enter Employee ID: "))
            manager.search_employee(emp_id)

        elif choice == "4":
            emp_id = int(input("ID: "))
            new_salary = float(input("New Salary: "))
            manager.update_employee(emp_id, new_salary)

        elif choice == "5":
            emp_id = int(input("ID: "))
            manager.delete_employee(emp_id)

        elif choice == "6":
            manager.save_data()
            print("Exiting system...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()