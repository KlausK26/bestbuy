# 16.11.2026

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = False

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        if self.quantity > 0:
            self.active = True
        else:
            self.active = False
        return self.active

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Quantity is too big")
        else:
            self.quantity -= quantity  # reduce quantity
        return float(quantity * self.price)
