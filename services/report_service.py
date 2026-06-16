class ReportService:

    @staticmethod
    def employee_count(employees):
        return len(employees)

    @staticmethod
    def average_salary(employees):

        total = sum(emp.salary for emp in employees)

        return total / len(employees)

    @staticmethod
    def department_report(employees):

        report = {}

        for emp in employees:

            dept = emp.department

            report[dept] = report.get(dept, 0) + 1

        return report