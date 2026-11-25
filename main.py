# 24.11 2026
import store, products   # Reihenfolge beachten

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def print_menu():
    print("")
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. quit")

def show_products():
    products = best_buy.get_all_products()
    num = 0
    print("------")
    for product in products:
        num += 1
        print(f"{num}. {product.name}, Price: ${product.price}, "
              f"Quantity: {product.quantity} ")
    print("------")

def start(store):
    while True:
        print_menu()
        try:
            selected = int(input("Please choose a number: "))
            if selected == 1:    # list product amount
                show_products()

            if selected == 2:    # total_quantity
                total = best_buy.get_total_quantity()
                print("Total of {} items in store".format(total))

            if selected == 3:  # make an order
                show_products()
                shopping_cart = []
                print("When you want to finish order, enter empty text.")  # was genau ??
                while True:
                    try:
                        index = int(input("Which product # do you want? "))
                        products = best_buy.get_all_products()
                        print(products[index - 1].name, products[index - 1].quantity)

                        if index != " ":
                            amount = int(input("What amount do you want? "))

                        if type(amount) != int:
                            print("Error adding product!")

                        if amount < products[index - 1].quantity:
                            total = store.order([(products[index - 1], amount)])
                            shopping_cart.append([products[index - 1]])
                            print("Product added to list!\n")

                    except ValueError:  # end order
                        print("Order made! Total payment: ", total)
                        break

            if selected == 4:
                break

        except ValueError:
                    print("Error with your choice! Try again!")

def main():
    start(best_buy)

main()