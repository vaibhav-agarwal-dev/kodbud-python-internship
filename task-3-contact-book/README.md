# Task 3: CLI Contact Book

A clean and interactive command-line interface (CLI) Contact Book application built using pure Python. It stores contact information (Name, Phone Number, and optional Email) in-memory using a list of dictionaries.

## Features

- **Add Contact**: Collects a new contact's details with validations:
  - Ensures name is not empty and is unique.
  - Validates that the phone number is numeric and within standard length (7-15 digits).
  - Validates optional email format (basic `@` and domain dot check).
- **View Contacts**: Displays all stored contacts in a formatted table.
- **Search Contacts**: Searches by name with case-insensitive and partial string matching.
- **Delete Contact**: Removes a contact matching the exact name after explicit user confirmation.
- **Error Handling**: Gracefully handles empty contact list, invalid inputs, and wrong menu choices.

## Prerequisites

- **Python 3.x** installed.

## How to Run

1. Open your terminal/command prompt.
2. Navigate to this task folder:
   ```bash
   cd task-3-contact-book
   ```
3. Run the Python file:
   ```bash
   python main.py
   ```

## Example Usage

### 1. Main Menu
```text
================ CONTACT BOOK ================
1. Add a New Contact
2. View All Contacts
3. Search Contact by Name
4. Delete a Contact
5. Exit
==============================================
Enter your choice (1-5):
```

### 2. View Contacts (Option 2)
```text
--- All Contacts ---
No.   | Name                      | Phone Number       | Email                    
-------------------------------------------------------------------------------
1     | Alice Smith               | 9876543210         | alice@example.com        
2     | Bob Jones                 | 123-456-7890       | bob@domain.org           
-------------------------------------------------------------------------------
```

### 3. Add Contact (Option 1)
```text
--- Add New Contact ---
Enter Name: Charlie Brown
Enter Phone Number: 5556667777
Enter Email (Optional, press Enter to skip): charlie@peanuts.com

Success: Contact for 'Charlie Brown' added successfully!
```

### 4. Search Contact (Option 3)
```text
--- Search Contacts ---
Enter name or part of the name to search: alice

Found 1 matching contact(s):
No.   | Name                      | Phone Number       | Email                    
-------------------------------------------------------------------------------
1     | Alice Smith               | 9876543210         | alice@example.com        
-------------------------------------------------------------------------------
```

### 5. Delete Contact (Option 4)
```text
--- Delete Contact ---
Enter the exact name of the contact to delete: Bob Jones

Found Contact: Bob Jones (123-456-7890)
Are you sure you want to delete 'Bob Jones'? (yes/no): yes
Success: Contact 'Bob Jones' has been deleted.
```
