"""
Task 3: Contact Book
A CLI-based Contact Book application built using Python.
This application allows users to add, view, search, and delete contacts.
Contacts are stored in-memory using a list of dictionaries.
"""

import sys

def validate_phone(phone: str) -> bool:
    """
    Validates the phone number.
    Must be digits only and between 7 and 15 digits long.
    """
    # Remove common separators like spaces, hyphens, and parentheses for validation
    clean_phone = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    return clean_phone.isdigit() and 7 <= len(clean_phone) <= 15

def validate_email(email: str) -> bool:
    """
    Validates the email address.
    Basic check to see if it contains '@' and a domain dot, if not empty.
    """
    if not email:
        return True  # Email is optional
    
    if "@" not in email:
        return False
    
    parts = email.split("@")
    if len(parts) != 2:
        return False
        
    local_part, domain_part = parts[0], parts[1]
    if not local_part:
        return False
        
    if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
        return False
        
    return True

def add_contact(contacts: list):
    """
    Prompts the user to add a new contact to the contact book.
    Validates name uniqueness, phone number, and optional email format.
    """
    print("\n--- Add New Contact ---")
    
    # 1. Get and validate Name
    name = input("Enter Name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    # Check for duplicate name (case-insensitive)
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Error: A contact with the name '{name}' already exists.")
            return

    # 2. Get and validate Phone
    phone = input("Enter Phone Number: ").strip()
    if not phone:
        print("Error: Phone number cannot be empty.")
        return
    if not validate_phone(phone):
        print("Error: Invalid phone number. It should contain 7 to 15 digits.")
        return

    # 3. Get and validate Email
    email = input("Enter Email (Optional, press Enter to skip): ").strip()
    if email and not validate_email(email):
        print("Error: Invalid email format (example: user@example.com).")
        return

    # Create and add contact dictionary
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email if email else "N/A"
    }
    contacts.append(new_contact)
    print(f"\nSuccess: Contact for '{name}' added successfully!")

def view_contacts(contacts: list):
    """
    Displays all contacts in the contact book in a formatted layout.
    """
    print("\n--- All Contacts ---")
    if not contacts:
        print("The contact book is empty. Add some contacts first!")
        return

    # Table Header
    print(f"{'No.':<5} | {'Name':<25} | {'Phone Number':<18} | {'Email':<25}")
    print("-" * 79)
    
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx:<5} | {contact['name']:<25} | {contact['phone']:<18} | {contact['email']:<25}")
    print("-" * 79)

def search_contacts(contacts: list):
    """
    Searches contacts by name using case-insensitive partial matching.
    """
    print("\n--- Search Contacts ---")
    if not contacts:
        print("The contact book is empty. Nothing to search.")
        return

    search_query = input("Enter name or part of the name to search: ").strip().lower()
    if not search_query:
        print("Error: Search query cannot be empty.")
        return

    results = []
    for contact in contacts:
        if search_query in contact['name'].lower():
            results.append(contact)

    if not results:
        print(f"No contacts found matching '{search_query}'.")
    else:
        print(f"\nFound {len(results)} matching contact(s):")
        print(f"{'No.':<5} | {'Name':<25} | {'Phone Number':<18} | {'Email':<25}")
        print("-" * 79)
        for idx, contact in enumerate(results, 1):
            print(f"{idx:<5} | {contact['name']:<25} | {contact['phone']:<18} | {contact['email']:<25}")
        print("-" * 79)

def delete_contact(contacts: list):
    """
    Deletes a contact by exact name (case-insensitive check).
    Requires verification before deletion.
    """
    print("\n--- Delete Contact ---")
    if not contacts:
        print("The contact book is empty. Nothing to delete.")
        return

    name_to_delete = input("Enter the exact name of the contact to delete: ").strip()
    if not name_to_delete:
        print("Error: Name cannot be empty.")
        return

    # Find the contact (case-insensitive comparison)
    target_contact = None
    for contact in contacts:
        if contact['name'].lower() == name_to_delete.lower():
            target_contact = contact
            break

    if not target_contact:
        print(f"Error: Contact with name '{name_to_delete}' not found.")
        return

    # Display contact details for confirmation
    print(f"\nFound Contact: {target_contact['name']} ({target_contact['phone']})")
    confirm = input(f"Are you sure you want to delete '{target_contact['name']}'? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        contacts.remove(target_contact)
        print(f"Success: Contact '{target_contact['name']}' has been deleted.")
    else:
        print("Deletion canceled.")

def main():
    """
    Main loop for the CLI menu interface.
    """
    contacts = []
    
    # Pre-populate with some sample contacts for ease of review
    contacts.append({"name": "Alice Smith", "phone": "9876543210", "email": "alice@example.com"})
    contacts.append({"name": "Bob Jones", "phone": "123-456-7890", "email": "bob@domain.org"})

    while True:
        print("\n================ CONTACT BOOK ================")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete a Contact")
        print("5. Exit")
        print("==============================================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("\nThank you for using Contact Book. Goodbye!")
            sys.exit(0)
        else:
            print("\nError: Invalid choice. Please select a valid option between 1 and 5.")

if __name__ == "__main__":
    main()
