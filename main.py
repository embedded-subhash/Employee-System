from services.employee_manager import EmployeeManager
from services.auth_service import AuthService
from services.report_service import ReportService
from utils.helper import print_header, get_current_time
from decorators.permissions import admin_required
from utils.logger import logger
from models.employee import Employee


@admin_required
def delete_permission(current_user):
    return True


def main():

    print_header("EMPLOYEE MANAGEMENT SYSTEM")
    print("Current Time:", get_current_time())

    logger.info("Application Started")

    # Authentication
    auth = AuthService()

    print("\nLOGIN")
    print("-" * 20)

    username = input("Username: ")
    password = input("Password: ")

    current_user = auth.login(username, password)

    if current_user is None:

        logger.warning(
            f"Invalid Login Attempt: {username}"
        )

        print("Invalid Username or Password")
        return

    print(f"\nWelcome {current_user.username}")
    print(f"Role: {current_user.role}")

    manager = EmployeeManager()
    report_service = ReportService()

    manager.load_data()

    while True:

        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee Salary")
        print("5. Delete Employee")
        print("6. Save & Exit")
        print("7. Employee Reports")

        choice = input("Enter choice: ")

        # Add Employee
        if choice == "1":

            if current_user.role not in ["Admin", "HR"]:
                print("Access Denied.")
                continue

            emp_id = int(input("ID: "))
            name = input("Name: ")
            email = input("Email: ")
            dept = input("Department: ")
            salary = float(input("Salary: "))
            exp = int(input("Experience: "))

            emp = Employee(
                emp_id,
                name,
                email,
                dept,
                salary,
                exp
            )

            manager.add_employee(emp)

            logger.info(
                f"Employee Added - ID:{emp_id}"
            )

        # View Employees
        elif choice == "2":

            manager.view_employees()

        # Search Employee
        elif choice == "3":

            emp_id = int(
                input("Enter Employee ID: ")
            )

            manager.search_employee(emp_id)

        # Update Employee
        elif choice == "4":

            if current_user.role not in ["Admin", "HR"]:
                print("Access Denied.")
                continue

            emp_id = int(input("ID: "))
            new_salary = float(
                input("New Salary: ")
            )

            manager.update_employee(
                emp_id,
                new_salary
            )

            logger.info(
                f"Employee Updated - ID:{emp_id}"
            )

        # Delete Employee
        elif choice == "5":

            if not delete_permission(
                current_user
            ):
                continue

            emp_id = int(
                input(
                    "Enter Employee ID to delete: "
                )
            )

            manager.delete_employee(emp_id)

            logger.info(
                f"Employee Deleted - ID:{emp_id}"
            )

        # Reports
        elif choice == "7":

            if current_user.role not in ["Admin", "HR"]:
                print("Access Denied.")
                continue

            report_service.total_employees(
                manager.employees
            )

            report_service.department_wise_report(
                manager.employees
            )

            report_service.highest_salary_employee(
                manager.employees
            )

            report_service.average_salary(
                manager.employees
            )

            report_service.experience_statistics(
                manager.employees
            )

        # Save and Exit
        elif choice == "6":

            manager.save_data()

            logger.info(
                "Application Closed"
            )

            print("Exiting system...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()