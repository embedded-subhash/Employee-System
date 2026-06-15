import json
from models.user import User


class AuthService:

    def login(self, username, password):

        try:

            with open("data/users.json", "r") as file:
                users = json.load(file)

            for user in users:

                if (
                    user["username"] == username
                    and user["password"] == password
                ):

                    return User(
                        user["username"],
                        user["password"],
                        user["role"]
                    )

            return None

        except FileNotFoundError:
            print("users.json not found")
            return None