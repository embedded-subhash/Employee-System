import unittest
from models.employee import Employee
import services.employee_service as es


class TestReports(unittest.TestCase):

    def setUp(self):
        es.reset_employees()

        self.emp1 = Employee(1, "John", "john@test.com", "IT", 50000, 2)
        self.emp2 = Employee(2, "Jane", "jane@test.com", "HR", 60000, 5)

        es.add_employee(self.emp1)
        es.add_employee(self.emp2)

    def test_employee_count(self):
        self.assertEqual(es.get_employee_count(), 2)

    def test_average_salary(self):
        avg = es.get_average_salary()
        expected = (50000 + 60000) / 2
        self.assertEqual(avg, expected)

    def test_employee_bonus(self):
        bonus = es.get_employee_bonus(1)
        self.assertTrue(bonus > 0)

    def test_total_salary(self):
        total = es.get_total_salary(1)
        self.assertEqual(total, 50000 + (50000 * 0.05))

    def test_invalid_employee(self):
        self.assertIsNone(es.get_employee_bonus(999))
        self.assertIsNone(es.get_total_salary(999))


if __name__ == "__main__":
    unittest.main()