emails = [
    "  Ali.Rahimi@Gmail.com",
    "sara@company.ca",
    "bad-email.com",
    "omar@@x.com",
    "lina@company.ca ",
]

domains = set()

for email in emails:
    # 1. Clean the email
    email = email.strip().lower()

    # 2. Validate the email
    if email.count("@") == 1:
        user, domain = email.split("@")

        if "." in domain:
            # 3. Print user and domain
            print(f"{user} @ {domain}")

            # 4. Store unique domains
            domains.add(domain)
        else:
            print(f"{email} → INVALID")
    else:
        print(f"{email} → INVALID")

# 5. Print unique, sorted domains
print("Domains:", ", ".join(sorted(domains)))
