import Products
import Store

# Setup initial stock of inventory
product_list = [
    Products.Product("MacBook Air M2", price=1450, quantity=100),
    Products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Products.Product("Google Pixel 7", price=500, quantity=250),
]
best_buy = Store.Store(product_list)


def menu():
    """Display the store menu options."""
    print(
        """
    ******** Store Menu *********
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """
    )


def list_products():
    """List all products in the store."""
    print("Available products:")
    for product in best_buy.get_all_products():
        product.show()


def show_total_quantity():
    """Show the total quantity of all products in the store."""
    print(f"Total quantity of all products in store: {best_buy.get_total_quantity()}")


def make_order():
    """Handle the process of making an order."""
    print("Available products:")
    products = best_buy.get_all_products()

    # Display products with numbers
    for product_index, product in enumerate(products, start=1):
        print(
            f"{product_index}. {product.name}, Price: ${product.price}, "
            f"Quantity: {product.quantity}"
        )

    print("------")
    print("When you want to finish the order, enter an empty text.")

    shopping_list = []
    while True:
        product_number = input("Which product do you want? ").strip()

        # Check if the user wants to finish the order
        if not product_number:
            break

        # Validate product number
        if product_number.isdigit():
            product_number = int(product_number)
            if 1 <= product_number <= len(products):
                selected_product = products[product_number - 1]  # Get the product by index
                quantity = input(f"How many of '{selected_product.name}' do you want? ").strip()

                if quantity.isdigit():
                    quantity = int(quantity)
                    shopping_list.append((selected_product, quantity))
                else:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Invalid product number. Please choose a valid number from the list.")
        else:
            print("Invalid input. Please enter a number.")

    # Process the order
    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"Order successful! Total price: ${total_price}")
        except ValueError as e:
            print(f"Order failed: {e}")
    else:
        print("No items were ordered.")


def start():
    """Main loop to handle user interactions with the store."""
    while True:
        menu()
        try:
            user_choice = int(input("Please choose a number: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if user_choice == 1:
            list_products()
        elif user_choice == 2:
            show_total_quantity()
        elif user_choice == 3:
            make_order()
        elif user_choice == 4:
            print("Exiting the store. Thank you!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    start()

