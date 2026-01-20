contacts = []

while True:
    print("\n=== Contact Book ===")
    print("1 - Add Contact")
    print("2 - View Contacts")
    print("3 - Search Contacts")
    print("4 - Delete Contact")
    print("5 - Quit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "5":
        print("Goodbye!")
        break

    elif choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        contact = {
            "name": name,
            "phone": phone 
        }

        contacts.append(contact)
        print(f"Added contact: {name} ({phone})")

    elif choice == "2":
        if not contacts:
            print("No contacts saved yet.")
        else:
            print("\nContacts:")
            for i, c in enumerate(contacts, start=1):
                print(f"{i}. {c['name']} - {c['phone']}")
    
    elif choice == "3":
        if not contacts:
            print("No contacts saved yet.")
        else:
            search = input("Search name: ").strip().lower()
            found = False

            for i, c in enumerate(contacts, start=1):
                if search in c["name"].lower():
                    print(f"{i}. {c['name']} - {c['phone']}")
                    found = True
            
            if not found:
                print("No matching contacts found.")

    elif choice == "4":
        if not contacts:
            print("No contacts saved yet.")
        else:
            print("\nContacts:")
            for i, c in enumerate(contacts, start=1):
                print(f"{i}. {c['name']} - {c['phone']}")
            
            delete_num = input("Enter the number to delete (or type 'cancel'): ").strip().lower()

            if delete_num == "cancel":
                print("Deletion cancelled.")
            else:
                delete_num = int(delete_num)

                if 1 <= delete_num <= len(contacts):
                    removed = contacts.pop(delete_num - 1)
                    print(f"Deleted: {removed['name']} ({removed['phone']})")
                else:
                    print("Invalid number.")



    else:
        print("Invalid choice. Please select 1-5.")