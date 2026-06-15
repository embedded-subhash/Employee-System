# services/authentication_service.py

_users = {
    "admin": "admin123",
    "user": "user123"
}


# ---------------------------
# LOGIN FUNCTION
# ---------------------------
def login(username, password):
    if username not in _users:
        return False

    return _users[username] == password


# ---------------------------
# REGISTER USER
# ---------------------------
def register(username, password):
    if username in _users:
        return False

    _users[username] = password
    return True


# ---------------------------
# RESET USERS (for tests)
# ---------------------------
def reset_users():
    global _users
    _users = {
        "admin": "admin123",
        "user": "user123"
    }


# ---------------------------
# OPTIONAL: CHECK AUTH
# ---------------------------
def is_authenticated(username, password):
    return login(username, password)