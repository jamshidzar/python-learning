# Drill 1. From numbers = [3, 8, 11, 14, 7], make a list of "even" or "odd" for each number.

from matplotlib.style import available


numbers = [3, 8, 11, 14, 7]
even_odd = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(even_odd)

## Drill 2. From this list, make "in stock" or "sold out" for each item:

stock = [0, 5, 0, 12, 3]

available = ["in stock" if n > 0 else "out of stock" for n in stock]

print(available)

##Drill 3. Free shipping (0) on orders of 100 or more, otherwise shipping costs 10:
prices = [20, 120, 45, 300]
shiping = [0 if n > 100 else 10 for n in prices]
print(shiping)
