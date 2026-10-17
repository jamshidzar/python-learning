def create_inventory(items):
    return add_items({}, items)


def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    inventory.pop(item, None)
    return inventory


def low_stock(inventory, limit):
    result = []
    for key, value in inventory.items():
        if value < limit:
            result.append(key)

    return sorted(result)


print(create_inventory(["apple", "milk", "apple", "bread", "apple"]))
print(create_inventory([]))

print(add_items({"apple": 3, "milk": 1}, ["apple", "bread", "bread"]))
print(add_items({"apple": 3}, []))

print(decrement_items({"apple": 2, "milk": 1}, ["apple", "milk", "milk", "bread"]))
print(decrement_items({"apple": 1}, []))

print(remove_item({"apple": 3, "milk": 1}, "milk"))
print(remove_item({"apple": 3}, "bread"))


print(low_stock({"apple": 5, "milk": 1, "bread": 0, "eggs": 2}, 3))
print(low_stock({"apple": 5}, 3))
print(low_stock({}, 3))
