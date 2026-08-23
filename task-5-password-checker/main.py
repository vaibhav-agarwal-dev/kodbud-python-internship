import re
import sys

def check_password_strength(password: str) -> tuple[bool, list[str]]:
    """
    Checks the strength of a password against standard criteria.
    
    Criteria:
    1. Minimum length of 8 characters.
    2. At least one uppercase letter (A-Z).
    3. At least one number (0-9).
    4. At least one special character (e.g., !, @, #, $, etc.).
    
    Args:
        password (str): The password string to evaluate.
        
    Returns:
        tuple[bool, list[str]]: A tuple containing:
            - is_strong (bool): True if all criteria are met, False otherwise.
            - missing_requirements (list): A list of descriptions of the requirements that were not met.
    """
    missing_requirements = []

    # 1. Check minimum length
    if len(password) < 8:
        missing_requirements.append(f"Minimum length of 8 characters (current length: {len(password)})")

    # 2. Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        missing_requirements.append("At least one uppercase letter (A-Z)")

    # 3. Check for at least one number
    if not re.search(r'[0-9]', password):
        missing_requirements.append("At least one number (0-9)")

    # 4. Check for at least one special character
    # [^a-zA-Z0-9] matches any character that is NOT a letter or a number.
    if not re.search(r'[^a-zA-Z0-9]', password):
        missing_requirements.append("At least one special character (e.g., !, @, #, $, %, etc.)")

    is_strong = len(missing_requirements) == 0
    return is_strong, missing_requirements

def main():
    """
    Main function to run the command-line interface for the password checker.
    """
    print("=" * 60)
    print("            PASSWORD STRENGTH CHECKER (Task 5)            ")
    print("=" * 60)
    print("Requirements for a strong password:")
    print("  1. Minimum 8 characters in length")
    print("  2. Contains at least one uppercase letter (A-Z)")
    print("  3. Contains at least one number (0-9)")
    print("  4. Contains at least one special character (e.g., !, @, #, etc.)")
    print("=" * 60)
    print("Type 'exit' to quit the application.\n")

    while True:
        try:
            # Prompt the user for input
            password = input("Enter a password to check: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nExiting application. Goodbye!")
            break

        # Check if the user wants to exit
        if password.strip().lower() == "exit":
            print("Exiting application. Goodbye!")
            break

        # Handle empty/whitespace-only input gracefully (Error-safe behavior)
        if not password.strip():
            print("Error: Password input cannot be empty or contain only whitespace. Please try again.\n")
            continue

        # Evaluate the password
        is_strong, missing = check_password_strength(password)

        # Print the results
        if is_strong:
            print("\nResult: Strong")
            print("Success: This password meets all security requirements!")
        else:
            print("\nResult: Weak")
            print("Missing Requirements:")
            for req in missing:
                print(f"  - {req}")
        
        print("-" * 60 + "\n")

if __name__ == "__main__":
    main()
