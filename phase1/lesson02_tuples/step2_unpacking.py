##Drill 1

from numpy import average


order = (1001, "laptop", 2, 899.99)
ide, product, quantity, price = order

print(f"Order {ide}: {quantity} x {product} at ${price}")

# Drill 2.
x = 10
y = 20
x, y = y, x

print(x, y)

## Drill 3. Run a, b = (1, 2, 3). Read the last line of the error. Then fix it using *.

a, *b = (1, 2, 3)

print(a, b)

## Drill 4. Write a function stats(numbers) that returns the total and the average. Call it with [10, 20, 30, 40] and unpack the result into two variables. Print both.


def stats(numbers):
    return sum(numbers), (sum(numbers) / len(numbers))


total, average = stats([10, 20, 30, 40])
print(total, average)


### Drill 5. Given:employees = [("Ali", "backend", 70000), ("Sara", "devops", 85000), ("Omar", "frontend", 65000)]

##Loop with unpacking and print only the people earning more than 68000, like:
# Ali (backend): $70000
employees = [
    ("Ali", "backend", 70000),
    ("Sara", "devops", 85000),
    ("Omar", "frontend", 65000),
]


for name, job, salary in employees:
    if salary > 68000:
        print(f"{name} ({job}): $${salary}")


## Drill 6. From log = ("2026-10-18", "ERROR", "db", "connection timeout", "retrying"), get the date into date and everything after it into details, in one line. Print both. What type is details?


log = ("2026-10-18", "ERROR", "db", "connection timeout", "retrying")

date, *details = log
print(date)
print(details)

## Next is Drill 7: from row = (7, "Nadia", "nadia@mail.com", "Halifax"), get only the name and city in one line, using _ for the values you skip.

row = (7, "Nadia", "nadia@mail.com", "Halifax")

_, name, _, city = row
