from functools import wraps

def require_admin(func: function):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_inventory(role):
    print("Access granted to tea inventory")

access_inventory("user")
access_inventory("admin")


# def login(func: function):
#     @wraps(func)