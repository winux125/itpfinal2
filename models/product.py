class Product:
    # product class
    def __init__(self, id: int, name: str, price: float, quantity: int):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount: int):
        # change the stock amount
        if self.quantity + amount < 0:
            raise ValueError("Insufficient stock.")
        self.quantity += amount

    def to_dict(self) -> dict:
        # return a dict for json
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    def __str__(self):
        return f"[{self.id}] {self.name} - ${self.price:.2f} (In Stock: {self.quantity})"
