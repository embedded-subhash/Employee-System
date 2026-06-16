import unittest
from services.auth_service import AuthService

class TestAuthentication(unittest.TestCase):

    def test_successful_login(self):
        self.assertTrue(
            AuthService.login(
                "admin",
                "admin123"
            )
        )

    def test_wrong_password(self):
        self.assertFalse(
            AuthService.login(
                "admin",
                "wrong"
            )
        )

    def test_unauthorized_access(self):
        self.assertFalse(
            AuthService.login(
                "hacker",
                "123"
            )
        )

if __name__ == "__main__":
    unittest.main()