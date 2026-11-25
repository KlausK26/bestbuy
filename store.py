# BestBuy Project 18.11.2026
class Store:
    """Class for storing products and their quantity"""
    def __init__(self, products_init):       # list of products
        self.product_list = []
        for product in products_init:
            self.product_list.append(product)

    def add_product(self, product ):
        """Add a product to the store"""
        self.product_list.append(product)

    def remove_product(self, product):
        """Remove a product from the store"""
        self.product_list.remove(product)

    def get_total_quantity(self):
        """get total number of all products in store"""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """get number of all products types in store"""
        all_products = []
        for product in self.product_list:
            all_products.append(product)
        return all_products

    def order(self, products):
        """buy products, tupels in list"""
        total_sum = 0
        for product,number in products:   # liste tupel argumente
            total_sum = total_sum + (product.price * number)   # 24.11
            product.quantity -= number   # 25.11 reduziert quantity
        return total_sum
