raw_names = ["  ali ", "SARA", "omAR  ", " lina"]
# for i, raw_name in enumerate(raw_names):
#     raw_names[i] = raw_name.strip().title()
#     print(raw_name.strip().title())
# print(raw_names)

# print((", ".join(raw_names)))

# clean_names = []

# for raw_name in raw_names:
#     clean_name = raw_name.strip().title()

#     clean_names.append(clean_name)

# print(clean_names)
# print(", ".join(clean_names))

clean_names = [raw_name.strip().title() for raw_name in raw_names]
print(clean_names)
print(", ".join(clean_names))
