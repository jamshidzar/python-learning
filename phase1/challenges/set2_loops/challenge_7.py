orders = """Order 1: coffee, muffin
Order 2: tea
Order 3: coffee, bagel, coffee
Order 4: cookie
Order 5: muffin, Coffee"""

order_lines = orders.splitlines()

item = input("Search for an item: ").strip().lower()

if not item:
    print("Please type an item to search for.")
else:
    lines_found = 0

    for line_number, line in enumerate(order_lines, start=1):
        if item in line.lower():
            print(f"Line {line_number}: {line}")
            lines_found += 1

    if lines_found > 0:
        total = orders.lower().count(item)
        print(f"Found on {lines_found} lines, {total} times in total.")
    else:
        print(f"No orders with {item}.")
