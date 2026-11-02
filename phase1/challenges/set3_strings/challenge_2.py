# order = "coffee x2, muffin x1,  tea x3 "

# pieces = order.split(",")
# total = 0
# print(pieces)

# for piece in pieces:
#     piece = piece.strip()  # "coffee x2"
#     name, qty_text = piece.split()  # "coffee", "x2"
#     qty = int(qty_text.replace("x", ""))  # "2" → 2

#     print(f"{name}: {qty}")
#     total += qty

# print(f"Total items: {total}")


order = "bagel:4 | cookie:12 | tea:1"

order_list = order.split("|")
print(order_list)

total = 0
for piece in order_list:
    piece = piece.strip()
    name, q = piece.split(":")
    qty = int(q)
    total += qty

    print(f"{name}: {q}")

print(total)
