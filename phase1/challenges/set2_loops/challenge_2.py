items = ["coffee", "muffin", "tea"]
prices = [3.50, 4.25, 2.00]
quantities = [2, 1, 3]
total_cost = 0
for item, price, quantity in zip(items, prices, quantities):
    total = price * quantity
    total_cost += total
    print(f"{item}: ${price:.2f} x {quantity} = ${total:.2f}")
print(f"Total cost: ${total_cost:.2f}")
