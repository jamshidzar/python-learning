phones = ["(902) 555-1234", "902.555.9876", "555-12", "902 555 abcd"]

for i in phones:
    clean_phones = []
    for b in i:
        if b.isdigit():
            clean_phones.append(b)
    together = "".join(clean_phones)
    if len(together) == 10:
        formated_phone = together[:3] + "-" + together[3:6] + "-" + together[6:]
        print(formated_phone)
    else:
        print(f"{i} → Invalid")
