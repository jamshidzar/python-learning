contacts = {}  # name -> {"phone": ..., "email": ...}

while True:
    print("1. Add  2. View  3. List all  4. Update  5. Delete  6. Search 7. Quit")
    choose = input("Choose an option: ")

    if choose == "1":
        name = input("Name: ").lower().strip()

        # Guard 1: empty name → stop
        if not name:
            print("The name cannot be empty.")
            continue

        # Guard 2: name exists → only continue on "y"
        if name in contacts:
            overwrite = (
                input(f"{name} already exists. Overwrite? (y/n): ").strip().lower()
            )
            if overwrite == "n":
                print("Not saved.")
                continue
            if overwrite != "y":
                print("Please answer with y (yes) or n (no).")
                continue

        # Everyone who reaches here gets saved: new names, and "y" answers
        phone = input("Phone: ").strip()
        formatted_phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
        email = input("Email: ").strip()
        contacts[name] = {"phone": formatted_phone, "email": email}
        print(f"Saved {name}.")

    elif choose == "2":
        name = input("Name: ").lower().strip()
        if not name:
            print("The name cannot be empty.")
        else:
            if name in contacts:
                # FIX: no loop. We only want this one contact.
                info = contacts[name]
                print(f"{name} | {info['phone']} | {info['email']}")
            else:
                print(f"No contact named {name}.")

    elif choose == "3":
        # Guard: nothing to list
        if not contacts:
            print("No contacts yet.")
            continue

        count = len(contacts)
        if count == 1:
            print("1 contact:")
        else:
            print(f"{count} contacts:")

        # sorted() gives the names (keys) in A–Z order
        for name in sorted(contacts):
            info = contacts[name]
            print(f"{name} | {info['phone']} | {info['email']}")

    elif choose == "4":
        name = input("Name: ").lower().strip()
        if not name:
            print("The name cannot be empty.")
        else:
            if name in contacts:
                new_phone = input("New phone (Enter to keep): ").strip()
                new_email = input("New email (Enter to keep): ").strip()

                # FIX: only change a field if the user typed something.
                # An empty string is False, so Enter skips the update.
                if new_phone:
                    formatted_phone = (
                        f"{new_phone[:3]}-{new_phone[3:6]}-{new_phone[6:]}"
                    )
                    contacts[name]["phone"] = formatted_phone
                if new_email:
                    contacts[name]["email"] = new_email

                print(f"Updated {name}.")
            else:
                # FIX: added the missing f, so {name} shows the real name
                print(f"No contact named {name}.")

    elif choose == "5":
        name = input("Name: ").lower().strip()
        if not name:
            print("The name cannot be empty.")
        else:
            if name in contacts:
                # FIX: we already checked the key exists, so plain del is enough
                del contacts[name]
                print(f"Deleted {name}.")
            else:
                print(f"No contact named {name}.")
    elif choose == "6":
        search = input("Search: ").lower().strip()
        if not search:
            print("The search cannot be empty.")
        else:
            found = False
            for name, info in contacts.items():
                if name.lower().startswith(search):
                    print(f"{name} | {info['phone']} | {info['email']}")
                    found = True
            if not found:
                print(f"No contacts starting with '{search}'.")

    elif choose == "7":
        print("Thanks, goodbye!")
        break

    else:
        # Catches "7", "-1", letters, empty Enter, or symbols
        print("Invalid choice, try again.")
