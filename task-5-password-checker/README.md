# Task 5: Password Strength Checker

A command-line Python application that checks the strength of a user-provided password against specific security requirements and reports any missing requirements when the password is weak.

## Features

* **Strength Assessment:** Classifies passwords as `Strong` or `Weak`.
* **Actionable Feedback:** Lists the requirements that are missing when a password is weak.
* **Regular Expressions:** Uses Python's built-in `re` module for pattern checking.
* **Interactive Console:** Allows multiple passwords to be tested in a single run.
* **Input Validation:** Handles empty and whitespace-only input gracefully.
* **Safe Exit:** Allows the user to exit using `exit` and handles `Ctrl+C`/`Ctrl+D` gracefully.

## Password Requirements

A password is classified as **Strong** when it satisfies all of these requirements:

1. **Minimum Length:** At least 8 characters.
2. **Uppercase Letter:** At least one uppercase letter (`A-Z`).
3. **Number:** At least one number (`0-9`).
4. **Special Character:** At least one special character, such as `!`, `@`, `#`, `$`, or `%`.

## Technologies Used

* Python 3
* `re` — Python's built-in regular expression module
* Python standard library only

## How to Run

Open a terminal in the `task-5-password-checker` directory and run:

```bash
python main.py
```

## Example Usage

### Weak Password

```text
============================================================
            PASSWORD STRENGTH CHECKER (Task 5)
============================================================
Requirements for a strong password:
  1. Minimum 8 characters in length
  2. Contains at least one uppercase letter (A-Z)
  3. Contains at least one number (0-9)
  4. Contains at least one special character (e.g., !, @, #, etc.)
============================================================
Type 'exit' to quit the application.

Enter a password to check: weak

Result: Weak
Missing Requirements:
  - Minimum length of 8 characters (current length: 4)
  - At least one uppercase letter (A-Z)
  - At least one number (0-9)
  - At least one special character (e.g., !, @, #, $, %, etc.)
------------------------------------------------------------
```

### Weak Password With One Missing Requirement

```text
Enter a password to check: Hello123

Result: Weak
Missing Requirements:
  - At least one special character (e.g., !, @, #, $, %, etc.)
------------------------------------------------------------
```

### Strong Password

```text
Enter a password to check: Hello123!

Result: Strong
Success: This password meets all security requirements!
------------------------------------------------------------
```

### Empty Input

```text
Enter a password to check:

Error: Password input cannot be empty or contain only whitespace. Please try again.
```

### Exit

```text
Enter a password to check: exit
Exiting application. Goodbye!
```

## How the Code Works

The application is organized into two main functions.

### 1. `check_password_strength(password)`

This function checks the password against all four requirements and returns:

```text
(is_strong, missing_requirements)
```

The checks are:

* **Length:**

```python
len(password) < 8
```

* **Uppercase letter:**

```python
re.search(r'[A-Z]', password)
```

* **Number:**

```python
re.search(r'[0-9]', password)
```

* **Special character:**

```python
re.search(r'[^a-zA-Z0-9]', password)
```

The `re.search()` function searches through the password for a matching regular-expression pattern.

### 2. `main()`

The `main()` function handles the command-line interaction.

It:

1. Displays the password requirements.
2. Asks the user to enter a password.
3. Handles empty or whitespace-only input.
4. Calls `check_password_strength()`.
5. Displays `Strong` or `Weak`.
6. Displays missing requirements when the password is weak.
7. Allows the user to enter multiple passwords.
8. Exits when the user enters `exit`.

## Project Structure

```text
task-5-password-checker/
├── main.py
└── README.md
```

## Internship Task

This project was completed as **Task 5: Password Strength Checker** for the Python Programming Internship at Kodbud.
