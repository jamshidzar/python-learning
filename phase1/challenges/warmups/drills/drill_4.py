items = ["tea", "coffee", "muffin"]
stock = [12, 0, 5]

for i, (item, quntity) in enumerate(zip(items, stock), start=1):
    if quntity == 0:
        print(f"{i}. {item} SOLD OUT")
    else:
        print(f"{i}. {item} ({quntity} Left)")
