names = ["ali", "sara", "omar"]
ages = [34, 28, 41]

# age = dict(zip(names, ages))
#
# print(age)

age_by_name = {}
# for i, name in enumerate(names):
#     age_by_name[name] = ages[i]

for key,value in zip(names, ages):
    age_by_name[key] = value

print(age_by_name)