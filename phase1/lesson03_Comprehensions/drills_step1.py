###Drill 1. Convert this loop to a comprehension:

# temps_c = [0, 20, 37, 100]
# temps_f = []
# for c in temps_c:
#     temps_f.append(c * 9 / 5 + 32)


temps_c = [0, 20, 37, 100]
temps_f = [(c * 9 / 5 + 32) for c in temps_c]

print(temps_f)

## Drill 2. From emails = ["Ali@Gmail.com", " SARA@yahoo.com ", "omar@HOTMAIL.com"], make a list where every email is stripped of spaces and lowercase.

emails = ["Ali@Gmail.com", " SARA@yahoo.com ", "omar@HOTMAIL.com"]

new_list = [email.lower().strip() for email in emails]
print(new_list)


## Drill 3. Make a list of the first letter of each name in ["Halifax", "Calgary", "Toronto"]

city = ["Halifax", "Calgary", "Toronto"]

print(city[0][1])

new_city = [i[0] for i in city]
print(new_city)


## Drill 4

nums = [1, 2, 3]
doubled = [n * 2 for x in nums]
