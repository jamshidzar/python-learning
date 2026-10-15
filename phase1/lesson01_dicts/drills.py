# Drill 1: make a car dictionary and print the model
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020,
}
print(car["model"])

print(car.get("color", "red"))  # Using get() method to color


prices = {"apple": 1.5, "bread": 3, "apple": 2}
print(prices["apple"])  # prediction:
print("milk" in prices)  # prediction:
print(prices.get("milk", 0))  # prediction:
