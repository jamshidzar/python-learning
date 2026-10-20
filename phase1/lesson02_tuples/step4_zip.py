## Drill 1. Given names = ["Ali", "Sara", "Omar"] and scores = [85, 92, 78], print each name with its score, like Ali: 85.


names = ["Ali", "Sara", "Omar"]
scores = [85, 92, 78]

for i, b in zip(names, scores):
    print(f"{i}: {b}")

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} {score}. ")


# @Drill 2. Given subjects = ("math", "python", "english") and grades = (90, 88, 75), build a dict report from them using zip, then print it.

subjects = ("math", "python", "english")
grades = (90, 88, 75)

# first way
print(dict(zip(subjects, grades)))
dic = {}
# second way
for key, value in zip(subjects, grades):
    dic[key] = value
print(dic)


## Drill 3. Given names and scores from Drill 1, print the rank and name for each. Use enumerate and zip together, like 1. Ali 85.


## Drill 4. Given a = [1, 2, 3, 4] and b = [10, 20, 30, 40], print the sum of each pair. Expected: 11, 22, 33, 44.

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

for i, q in zip(a, b):
    print(i + q)


##Drill 5. Given products = ("laptop", "mouse", "keyboard") and prices = (899.99, 25.5, 49.0), print only the products that cost more than 40.

products = ("laptop", "mouse", "keyboard")

prices = (899.99, 25.5, 49.0)

for product, price in zip(products, prices):
    if price > 40:
        print(product)


###Drill 6

students = ("Ali", "Sara", "Omar")
math = (85, 92, 78)
python = (90, 88, 80)
for student, m, p in zip(students, math, python):
    _average = (m + p) / 2

    print(f"{student}. {float(_average)}")
