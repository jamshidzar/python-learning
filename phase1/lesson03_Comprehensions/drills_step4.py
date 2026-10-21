## Drill 1. From words = ["python", "sql", "docker"], make a dict of each word and its length.

from matplotlib.style import available


words = ["python", "sql", "docker"]

length_words = {word: len(word) for word in words}
print(length_words)

## Drill 2. Keep only the items that are in stock:
inventory = {"apples": 0, "bread": 12, "milk": 0, "eggs": 30}
available = {key: value for key, value in inventory.items() if value > 0}
print(available)

# Drill 3. Raise every price by 10%, rounded to 2 decimals:
prices = {"coffee": 3.0, "bagel": 2.5, "juice": 4.0}

new_prices = {item: round(price * 1.10, 2) for item, price in prices.items()}
print(new_prices)
# Drill 4. Flip the dict so values become keys and keys become values:
codes = {"HFX": "Halifax", "YYC": "Calgary", "YYZ": "Toronto"}

flip = {value: key for key, value in codes.items()}
print(flip)
