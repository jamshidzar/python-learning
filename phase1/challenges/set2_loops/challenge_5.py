items = ["coffee", "tea", "muffin", "bagel", "cookie"]
prices = [3.50, 2.00, 4.25, 2.75, 1.50]

exit_number = len(items) + 1

print("========== MENU ==========")
for number, (item, price) in enumerate(zip(items, prices), start=1):
    print(f"{number}. {item} - ${price:.2f}")
print(f"{exit_number}. Exit")

while True:
    choice = input("Pick a number: ").strip()

    if not choice.isdigit():
        print("Please type a number.")
        continue

    number = int(choice)

    if number == exit_number:
        print("Exiting the menu.")
        break
    elif 1 <= number <= len(items):
        index = number - 1
        print(f"You chose {items[index]} (${prices[index]:.2f})")
    else:
        print(f"Pick a number between 1 and {exit_number}.")
