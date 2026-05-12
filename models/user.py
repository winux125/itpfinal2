class User:
    # base user
    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role

    def get_menu_options(self) -> list:
        # this will be overridden
        raise NotImplementedError("Subclasses must implement get_menu_options")

    def __str__(self):
        return f"User({self.username}, role={self.role})"


class Admin(User):
    # admin user
    def __init__(self, username: str):
        super().__init__(username, "admin")

    def get_menu_options(self) -> list:
        return [
            "View all products",
            "Search/Filter products",
            "Add a product",
            "Remove a product",
            "Update product stock",
            "View low stock report",
            "Logout",
            "Exit"
        ]


class Customer(User):
    # regular customer
    def __init__(self, username: str):
        super().__init__(username, "customer")

    def get_menu_options(self) -> list:
        return [
            "View all products",
            "Search/Filter products",
            "Logout",
            "Exit"
        ]
