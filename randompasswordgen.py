import string
import random

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    """
    Generate a random password based on the user-defined criteria.
    
    Args:
    length (int): Length of the password.
    use_lowercase (bool): Whether to include lowercase letters.
    use_uppercase (bool): Whether to include uppercase letters.
    use_digits (bool): Whether to include digits.
    use_special_chars (bool): Whether to include special characters.
    
    Returns:
    str: Generated password.
    """
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Initialize character set for password
    charset = ""

    # Add selected character sets to the password charset
    if use_lowercase:
        charset += lowercase_letters
    if use_uppercase:
        charset += uppercase_letters
    if use_digits:
        charset += digits
    if use_special_chars:
        charset += special_chars

    # Check if at least one character set is selected
    if not charset:
        print("Please select at least one character set.")
        return None

    # Generate password
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password criteria
    length = int(input("Enter the length of the password: "))
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate password
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)

    # Display the generated password
    if password:
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()



