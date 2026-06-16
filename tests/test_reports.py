import unittest

from models.employee import Employee
from services.report_service import ReportService

class TestReports(unittest.TestCase):

    def setUp(self):

        self.employees = [
            Employee(1,"A","a@gmail.com","IT",50000,2),
            Employee(2,"B","b@gmail.com","IT",60000,3),
            Employee(3,"C","c@gmail.com","HR",40000,1)
        ]

    def test_employee_count(self):
        self.assertEqual(
            ReportService.employee_count(
                self.employees
            ),
            3
        )

    def test_average_salary(self):
        self.assertEqual(
            ReportService.average_salary(
                self.employees
            ),
            50000
        )

    def test_department_report(self):

        result = ReportService.department_report(
            self.employees
        )

        self.assertEqual(result["IT"], 2)
        self.assertEqual(result["HR"], 1)

if __name__ == "__main__":
    unittest.main()