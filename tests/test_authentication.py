import unittest
import services.authentication_service as auth


class TestAuthentication(unittest.TestCase):

    def setUp(self):
        auth.reset_users()

    def test_successful_login(self):
        result = auth.login("admin", "admin123")
        self.assertTrue(result)

    def test_wrong_password(self):
        result = auth.login("admin", "wrongpass")
        self.assertFalse(result)

    def test_invalid_user(self):
        result = auth.login("ghost", "123")
        self.assertFalse(result)

    def test_register_user(self):
        result = auth.register("newuser", "pass123")
        self.assertTrue(result)

        self.assertTrue(auth.login("newuser", "pass123"))

    def test_duplicate_register(self):
        result = auth.register("admin", "admin123")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()