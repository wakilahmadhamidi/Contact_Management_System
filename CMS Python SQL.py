import sqlite3

class ContactManagementSystem:
    def __init__(self):
        self.conn = sqlite3.connect("contacts.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT,
                gender TEXT,
                address TEXT
            )
        ''')
        self.conn.commit()

    def add_contact(self, name, phone, email, gender, address):
        self.cursor.execute("INSERT INTO contacts (name, phone, email, gender, address) VALUES (?, ?, ?, ?, ?)", (name, phone, email, gender, address))
        self.conn.commit()

    def display_contacts(self):
        self.cursor.execute("SELECT * FROM contacts")
        contacts = self.cursor.fetchall()
        for contact in contacts:
            print(contact)

    def search_contact(self, name):
        self.cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
        contact = self.cursor.fetchone()
        if contact:
            print(contact)
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone, email, gender, address):
        self.cursor.execute("UPDATE contacts SET phone=?, email=?, gender=?, address=?WHERE name=?", (phone, email, gender, address, name))
        self.conn.commit()

    def delete_contact(self, name):
        self.cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
        self.conn.commit()

# Create an instance of the ContactManagementSystem class with an SQLite database
contact_system = ContactManagementSystem()

while True:
    print("-" * 25)
    print("Contact Management System")
    print("-" * 25)
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        gender = input("Enter gender: ")
        address = input("Enter address: ")
        contact_system.add_contact(name, phone, email, gender, address)
        print(f"Contact '{name}' added successfully.")

    elif choice == '2':
        contact_system.display_contacts()

    elif choice == '3':
        name = input("Enter name: ")
        contact_system.search_contact(name)

    elif choice == '4':
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        gender = input("Enter new gender: ")
        address = input("Enter new address: ")
        contact_system.update_contact(name, phone, email, gender, address)

    elif choice == '5':
        name = input("Enter name: ")
        contact_system.delete_contact(name)

    elif choice == '6':
        break

    else:
        print("Invalid choice. Try again.") 
    print("Thank you for using our Contact Management System.")
    print("By: Hamidi Developing Team")