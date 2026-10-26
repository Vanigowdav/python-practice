
import os
import json


def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
        return contacts
    else:
        return []


def save_contacts(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


def search_contact(contacts):
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact["name"].strip().lower() == name.lower():
            print("Contact found:", contact)
            return

    print("Contact not found")


def delete_contact(contacts):
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].strip().lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available")
        return

    for contact in contacts:
        print(contact)


contacts = load_contacts()

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View contacts")
    print("5. Exit")

    try: 
        choice = int(input("Enter your choice: "))
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            view_contacts(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    except ValueError:
        print("Please enter a valid number.")       
