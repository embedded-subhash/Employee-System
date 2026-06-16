import unittest
from models.employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp = Employee(
            101,
            "Subhash",
            "subhash@gmail.com",
            "Engineering",
            50000,
            3
        )

    def test_employee_creation(self):
        self.assertEqual(self.emp.name, "Subhash")
        self.assertEqual(self.emp.salary, 50000)

    def test_salary_calculation(self):
        self.assertEqual(self.emp.salary, 50000)

    def test_bonus_calculation(self):
        self.assertEqual(self.emp.calculate_bonus(), 5000)

    def test_invalid_employee_data(self):
        with self.assertRaises(ValueError):
            Employee(
                102,
                "",
                "test@gmail.com",
                "Engineering",
                -1000,
                2
            )

if __name__ == "__main__":
    unittest.main()