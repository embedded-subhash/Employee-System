class AuthService:

    users = {
        "admin": "admin123"
    }

    @classmethod
    def login(cls, username, password):

        if username not in cls.users:
            return False

        return cls.users[username] == password