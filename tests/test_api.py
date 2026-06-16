import unittest

from api.employee_api import (
    create_employee,
    employee_report
)

from services.employee_service import reset_employees


class TestAPI(unittest.TestCase):

    def setUp(self):
        reset_employees()

    def test_create_employee(self):

        response = create_employee({
            "employee_id": 101,
            "name": "Subhash",
            "email": "subhash@gmail.com",
            "department": "ECE",
            "salary": 50000,
            "experience": 3
        })

        self.assertEqual(response["status"], 201)

    def test_employee_report(self):

        create_employee({
            "employee_id": 101,
            "name": "Subhash",
            "email": "subhash@gmail.com",
            "department": "ECE",
            "salary": 50000,
            "experience": 3
        })

        report = employee_report()

        self.assertEqual(report["employee_count"], 1)


if __name__ == "__main__":
    unittest.main()