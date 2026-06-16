import unittest
from models.employee import Employee


class TestEmployee(unittest.TestCase):

    def test_employee_creation(self):
        emp = Employee(101, "jhon", "jhon@gmail.com", "IT", 50000, 3)

        self.assertEqual(emp.employee_id, 101)
        self.assertEqual(emp.name, "jhon")
        self.assertEqual(emp.department, "IT")
        self.assertEqual(emp.salary, 50000)

    def test_salary_calculation(self):
        emp = Employee(102, "jane", "jane@gmail.com", "HR", 60000, 5)
        self.assertGreater(emp.salary, 0)

    def test_bonus_calculation(self):
        emp = Employee(103, "doe", "doe@gmail.com", "Finance", 50000, 3)
        expected_bonus = 5000  # 10%
        self.assertEqual(emp.calculate_bonus(), expected_bonus)

    def test_invalid_employee_data(self):
        with self.assertRaises(ValueError):
            Employee(104, "invalid", "invalidemail", "IT", -1000, 2)


if __name__ == "__main__":
    unittest.main()