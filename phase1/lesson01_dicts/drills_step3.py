# Drill 1
stock = {"apple": 10, "bread": 3, "milk": 8, "eggs": 2}

for item, quantity in stock.items():
    print(f"{item} → {quantity} left")


# Drill 2


total_of_items = sum(stock.values())
print(total_of_items)  # prediction: 23

## Drill 3

for item in stock:
    if stock[item] < 5:
        print(f"{item} is in stock")

##Drill 4
letters = "Banana"
letter_count = {}
for letter in letters.lower():
    letter_count[letter] = letter_count.get(letter, 0) + 1
print(letter_count)


prices = {"tea": 2, "cake": 5}
for name, price in prices.items():
    prices[name] = price * 2
print(prices)  # prediction:{'tea': 4, 'cake': 10}
