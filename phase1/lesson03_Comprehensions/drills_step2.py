# Drill 1. From scores = [45, 82, 67, 90, 38, 75], keep only passing scores (60 or above).

from numpy import empty


scores = [45, 82, 67, 90, 38, 75]

passing_grade = [n for n in scores if n >= 60]

print(passing_grade)

# Drill 2. From this list, keep only the .txt files:
files = ["notes.txt", "photo.png", "report.txt", "song.mp3"]

new_file = [n for n in files if n.endswith(".txt")]
print(new_file)

##Drill 3. From these orders, make a list of orders over 100, each with 15% tax added:
orders = [12.5, 150.0, 89.99, 230.0, 45.0]
orders_with_tax = [order * 1.15 for order in orders if order > 100]

print(orders_with_tax)

##Drill 4. Get a clean list: stripped, lowercase, and no empty entries.

raw = [" ali ", "", "  ", "SARA", " omar"]

clean_names = [name.strip().lower() for name in raw if name.strip()]
print(clean_names)


tags = ["  Python", "", "FastAPI  ", "   ", "SQL"]
clean_tags = [tag.strip().lower() for tag in tags if tag.strip()]
print(clean_tags)
