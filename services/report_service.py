class ReportService:

    def total_employees(self, employees):

        print("\nTotal Employees:", len(employees))

    def highest_salary_employee(self, employees):

        if not employees:
            print("No employees found.")
            return

        highest = max(
            employees,
            key=lambda emp: emp.salary
        )

        print("\nHighest Salary Employee")
        highest.display_details()

    def department_wise_report(self, employees):

        report = {}

        for emp in employees:

            dept = emp.department

            if dept in report:
                report[dept] += 1
            else:
                report[dept] = 1

        print("\nDepartment Wise Report")

        for dept, count in report.items():
            print(f"{dept}: {count}")

    def average_salary(self, employees):

        if not employees:
            print("No employees found.")
            return

        total = sum(
            emp.salary
            for emp in employees
        )

        avg = total / len(employees)

        print(
            f"\nAverage Salary: {avg:.2f}"
        )

    def experience_statistics(self, employees):

        if not employees:
            print("No employees found.")
            return

        highest = max(
            emp.experience
            for emp in employees
        )

        lowest = min(
            emp.experience
            for emp in employees
        )

        print("\nExperience Statistics")
        print("Highest Experience:", highest)
        print("Lowest Experience:", lowest)