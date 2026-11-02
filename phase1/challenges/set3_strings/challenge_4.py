usernames = ["ali_99", "Sara", "9omar", "li", "jamshid.zar", "  Kim  "]

for raw in usernames:
    name = raw.strip().lower()

    if len(name) < 3:
        print(f"{name} → INVALID: too short")
    elif len(name) > 12:
        print(f"{name} → INVALID: too long")
    elif not name[0].isalpha():
        print(f"{name} → INVALID: must start with a letter")
    else:
        all_ok = True
        for char in name:
            if not (char.isalnum() or char == "_"):
                all_ok = False
                break

        if all_ok:
            print(f"{name} → valid")
        else:
            print(f"{name} → INVALID: only letters, digits and _ allowed")
