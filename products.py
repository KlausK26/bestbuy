# 16.11.2026

class Product:
    """class for the products used in the Store"""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = False

    def get_quantity(self):
        """returns the quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """sets the quantity of the product"""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """checks if the product is active"""
        if self.quantity > 0:
            self.active = True
        else:
            self.active = False
        return self.active

    def deactivate(self):
        """deactivates the product"""
        self.active = False

    def show(self):
        """shows the product items"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """buys the product, number of it"""
        if quantity > self.quantity:
            raise ValueError("Quantity is too big")

        self.quantity -= quantity  # reduce quantity
        return float(quantity * self.price)
