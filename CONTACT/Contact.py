# Contact Book Application

class ContactBook:
    def __init__(self):
        self.contacts = []  # List to store contacts
#to add here personal details eg. divya 8269183893 divyapaikra7636@gmail.com 15/d
    def add_contact(self, name, phone, email, address):
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print(f"Contact '{name}' has been added.")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available!")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} | {contact['phone']}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact['name'].lower() or keyword in contact['phone']]
        if results:
            print("\nSearch Results:")
            for contact in results:
                self.show_contact_details(contact)
        else:
            print("\nNo contacts found with that keyword.")

    def show_contact_details(self, contact):
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

    def update_contact(self, index, name, phone, email, address):
        try:
            self.contacts[index - 1].update({"name": name, "phone": phone, "email": email, "address": address})
            print(f"Contact {index} has been updated.")
        except IndexError:
            print("Invalid contact number. Please try again.")

    def delete_contact(self, index):
        try:
            removed_contact = self.contacts.pop(index - 1)
            print(f"Contact '{removed_contact['name']}' has been deleted.")
        except IndexError:
            print("Invalid contact number. Please try again.")


def main():
    contact_book = ContactBook()

    while True:
        print("\n=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search")
