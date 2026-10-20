fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

for rank, player in enumerate(["Ali", "Sara", "Omar"], start=1):
    print(f"{rank}. {player}")

# Drill 1. Given colors = ["red", "green", "blue"], print each color with its index starting at 0.

colors = ["red", "green", "blue"]

for i, b in enumerate(colors):
    print(i, b)

# Drill 2. Same list, numbered from 1, formatted like 1. red
for i, b in enumerate(colors, start=1):
    print(f"{i}. {b}")

## Drill 3. Given tasks = ("write tests", "fix bug", "deploy", "review PR") (note: a tuple this time), print only the tasks at even indexes (0, 2, ...).

tasks = ("write tests", "fix bug", "deploy", "review PR")

for i, b in enumerate(tasks):
    if i % 2 == 0:
        print(f"{i}. {b}")


## Drill 4. Given lines = ["import os", "", "def main():", " pass"], print the line number (starting at 1) of every empty line. Expected output: 2.


lines = ["import os", "", "def main():", " pass"]

for i, b in enumerate(lines, start=1):
    if b == "":
        print(i)


##Drill 5. Use enumerate on "Nadia". Print each index and character, but only where the index is greater than 2.

name = "Nadia"
for i, b in enumerate(name):
    if i > 2:
        print(f"{i}. {b}")

##Drill 6. Rewrite this without enumerate, using range(len(...)):
names = ("Ali", "Sara", "Omar")
for i, name in enumerate(names):
    print(f"{i}: {name.upper()}")

for i in range(len(names)):
    print(f"{i}: {names[i].upper()}")


# Drill 7 (think, then code). You have a tuple of 1000 log lines and want the line number of every line that contains "ERROR". Write the loop

log_lines = ("INFO started", "ERROR db down", "INFO retrying", "ERROR timeout")

for i, b in enumerate(log_lines, start=1):
    if "ERROR" in b:
        print(i)
