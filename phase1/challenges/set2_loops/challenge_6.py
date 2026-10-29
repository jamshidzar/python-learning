items = ["coffee", "tea", "muffin", "bagel", "cookie"]
old_prices = [3.50, 2.00, 4.25, 2.75, 1.50]
new_prices = [3.75, 2.00, 3.95, 2.75, 1.75]

unchanged = []

for item, old_price, new_price in zip(items, old_prices, new_prices):
    difference = abs(new_price - old_price)

    if new_price > old_price:
        print(f"{item}: up ${difference:.2f}")
    elif new_price < old_price:
        print(f"{item}: down ${difference:.2f}")
    else:
        unchanged.append(item)

print(f"Unchanged: {', '.join(unchanged)}")
