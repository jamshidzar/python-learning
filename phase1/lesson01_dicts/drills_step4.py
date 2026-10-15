order = {
    "id": 101,
    "customer": {"name": "Sara", "phone": "902-555-0101"},
    "items": [
        {"name": "burger", "price": 12.5},
        {"name": "fries", "price": 4.0},
    ],
}
#   Drill 1. Print the customer’s phone number.
print(order["customer"]["phone"])  # prediction: 902-555-0101

order["customer"]["name"] = "Sara K"
print(order)

order["items"].append({"name": "drink", "price": 2.5})
print(order)

for item in order["items"]:
    print(f"{item['name']}: ${item['price']}")

total = 0
for item in order["items"]:
    total += item["price"]
print(f"Total: ${total}")  # prediction: Total: $19.0

print(
    order.get("customer").get("email", "No email provided")
)  # prediction: No email provided


print(order["items"][1]["name"])  # prediction: burger
