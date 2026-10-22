"""
Café Order System: a CLI app where a customer views the menu, adds items to a cart,
and checks out with a receipt that includes 15% tax.
"""

TAX_RATE = 0.15

menu = {
    "coffee": 3.00,
    "tea": 2.50,
    "bagel": 2.75,
    "muffin": 3.25,
    "sandwich": 7.50,
}

cart = []


def show_menu(menu):
    print("--- MENU ---")

    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def add_to_cart(menu, cart):
    while True:
        item = (
            input("Enter an item to add to your cart (or 'done' to finish): ")
            .strip()
            .lower()
        )

        if item in menu:
            try:
                quantity = int(input(f"Enter the quantity for {item}: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer for quantity.")
                continue

            cart.append((item, quantity))
            print(f"Added {quantity} x {item} to your cart.")
        elif item == "done":
            print("Finished adding items to the cart.")
            break
        else:
            print("Item not found in the menu. Please try again.")


def show_cart(menu, cart):
    print("\n--- YOUR CART ---")

    if not cart:
        print("Your cart is empty.")
        return

    subtotal = 0.0
    for item, quantity in cart:
        price = menu[item]
        item_total = price * quantity
        subtotal += item_total
        print(f"{quantity} x {item} @ ${price:.2f} = ${item_total:.2f}")

    print(f"Subtotal: ${subtotal:.2f}")


def checkout(menu, cart):
    if not cart:
        print("Your cart is empty. Add items before checking out.")
        return

    print("\n======= RECEIPT =======")
    subtotal = 0.0
    for item, quantity in cart:
        price = menu[item]
        item_total = price * quantity
        subtotal += item_total
        print(f"{quantity} x {item} @ ${price:.2f} = ${item_total:.2f}")

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    print("-----------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (15%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("=======================")
    print("Thank you for your order!")

    cart.clear()


def main():
    while True:
        print("\n=== CAFÉ ===")
        print("1. Show menu")
        print("2. Add items")
        print("3. View cart")
        print("4. Checkout")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            add_to_cart(menu, cart)
        elif choice == "3":
            show_cart(menu, cart)
        elif choice == "4":
            checkout(menu, cart)
        elif choice == "5":
            print("Thanks for visiting. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")


main()
