contacts = []


def add_contact(contacts):
    name = input("Name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    phone = input("Phone: ").strip()
    if not phone.isdigit():
        print("Phone must contain only digits.")
        return
    contacts.append({"name": name, "phone": phone})
    print("Contact added.")


def show_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    for number, contact in enumerate(contacts, start=1):
        print(f"{number}. {contact['name']} - {contact['phone']}")


def search_contact(contacts):
    name = input("Name: ").strip().lower()
    if name == "":
        print("Please type a name.")
        return
    found = False
    for contact in contacts:
        if name in contact["name"].lower():
            print(f"Found: {contact['name']} - {contact['phone']}")
            found = True
    if not found:
        print("Not found")


def delete_contact(contacts):
    name = input("Name: ").strip().lower()
    if name == "":
        print("Please type a name.")
        return
    contact_to_delete = None
    for contact in contacts:
        if contact["name"].strip().lower() == name:
            contact_to_delete = contact
            break
    if contact_to_delete is None:
        print("Not found")
    else:
        contacts.remove(contact_to_delete)
        print("Deleted:", contact_to_delete["name"])


while True:
    print("\n1. Add  2. Search  3. Delete  4. Show all  5. Quit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        search_contact(contacts)
    elif choice == "3":
        delete_contact(contacts)
    elif choice == "4":
        show_contacts(contacts)
    elif choice == "5":
        break
    else:
        print("Invalid choice")