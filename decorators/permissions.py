def admin_required(func):

    def wrapper(current_user, *args, **kwargs):

        if current_user.role != "Admin":
            print("Access Denied. Admin Only.")
            return

        return func(current_user, *args, **kwargs)

    return wrapper