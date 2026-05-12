from functools import wraps

def admin_required(func):
    # check if user is admin
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.current_user or self.current_user.role != "admin":
            print("Access Denied: You must be an administrator to perform this action.")
            return
        return func(self, *args, **kwargs)
    return wrapper
