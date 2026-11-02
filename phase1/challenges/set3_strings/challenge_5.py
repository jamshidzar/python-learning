codes = ["AB-123", "XY-9", "cd-456", "QR-12a", "ZZ-000"]

for code in codes:
    if (
        len(code) == 6
        and code[:2].isalpha()
        and code[:2].isupper()
        and code[2] == "-"
        and code[3:].isdigit()
    ):
        print(f"{code} → valid")
    else:
        print(f"{code} → INVALID")
