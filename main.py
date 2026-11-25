# 24.11 2026
# Reihenfolge imports beachten
import store        # Store Klasse
import products     # Product Klasse

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)  # Erstellung einer Instanz

def print_menu():       # formatted view of then menu
    print("")
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def show_products():       # show list of products in store
    products_in_store = best_buy.get_all_products()
    num = 0
    print("------")
    for item in products_in_store:
        num += 1
        print(f"{num}. {item.name}, Price: ${item.price}, "
              f"Quantity: {item.quantity} ")
    print("------")

def start(store_in):    # init store view
    while True:         # main loop
        print_menu()
        try:
            selected = int(input("Please choose a number: "))
            if selected <= 0 or selected >= 5:     # only numbers (1..4)
                print("Error with your choice! Try again!")

            if selected == 1:    # list product amount
                show_products()

            if selected == 2:    # total_quantity
                total = best_buy.get_total_quantity()
                print("Total of {} items in store".format(total))

            if selected == 3:  # make an order
                show_products()
                shopping_cart = []
                total = 0

                # order loop
                print("When you want to finish order, enter empty text.")  # was genau ??
                while True:
                        index_text = input("Which product # do you want? ")
                        amount_text = input("What amount do you want? ")

                        if index_text == "" or amount_text == "":   # exit order loop
                            if total > 0:
                                print("********")
                                print("Order made! Total payment:", total)
                            break

                        if index_text.isdecimal() and amount_text.isdecimal():
                            index = int(index_text)
                            amount = int(amount_text)
                            products = best_buy.get_all_products()    # read all products

                            if index > 0 and amount < products[index - 1].quantity:   # check
                                total += store_in.order([(products[index - 1], amount)])
                                shopping_cart.append([products[index - 1]])
                                print("Product added to list!\n")
                        else:
                            print("Error adding product!")
                            print("")

            if selected == 4:   # quit app
                break

        except ValueError:
                    print("Error with your choice! Try again!")

def main():     # main function
    start(best_buy)

main()
