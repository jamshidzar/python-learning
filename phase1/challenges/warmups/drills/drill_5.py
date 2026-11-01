items = ["tea", "coffee", "muffin", "bagel", "cookie"]
stock = [12, 0, 5, 0, 8]

stock_index = []
total = 0
for i, q in enumerate(stock, start=1):
    if q == 0:
        stock_index.append(str(i))
    else:
        total += q

print(f"Sold out: {', '.join(stock_index)}\nTotal in stock: {total}")
