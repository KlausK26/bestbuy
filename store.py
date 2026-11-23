# BestBuy Project 18.11.2026
import products

class Store:
    def __init__(self, products_init):       # list of products
        self.product_list = []
        for product in products_init:
            #print(product.name)
            self.product_list.append(product)

    def add_product(self, product ):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):    # get number of products in store
        total_quantity = 0
        for product in self.product_list:
            total_quantity += 1
        return total_quantity

    def get_all_products(self):      # get number of all products in store
        All_products = []
        for product in self.product_list:
            All_products.append(product)
        return All_products

    def order(self, products):
        total_sum = 0
        for product,number in products:   # liste tupel argumente
            #print(product.price, number)
            total_sum += product.price * number   # 21.11.26
        return total_sum

bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac  = products.Product("MacBook Air M2", price=1450, quantity=100)

# instance of a store

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

#best_buy = Store([ bose, mac ])  # test
best_buy = Store(product_list)

pixel = products.Product("Google Pixel 7", price=500, quantity=250)
best_buy.add_product(pixel)
#print("Added Pixel:", best_buy.product_list)    # test add product
total_quant = best_buy.get_total_quantity()
print("Anzahl Producte:", total_quant)
best_buy.remove_product(pixel)  # test remove product

#total_prod = best_buy.get_all_products()
#print("Anz aller Prod im Store:" ,total_prod)

price = best_buy.order([(bose, 5)] )
print(f"Order costs: {price} dollars")
price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])    # should be
print(f"Order costs: {price} dollars")


# tests
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())

# Final test
best_buy.order([(products[0], 1), (products[1], 2)] )
print(best_buy.order([(products[0], 1), (products[1], 2)]))