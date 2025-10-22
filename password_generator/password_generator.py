"""
Simple Password Generator
This script generates a random password based on user-defined criteria such as length and inclusion of special characters

"""

import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

class PasswordGenerator:
    def __init__(self, use_special_chars, length=8):
        self.length = length
        self.use_special_chars = use_special_chars

    def generate_password(self):
        """
        Generate a random password based on the specified length and character set.
        
        """
        
        if self.use_special_chars:
            char_set = chars
        else:
            char_set = string.ascii_letters + string.digits
    
        password = ''.join(random.choice(char_set) for _ in range(self.length))
        return password


def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length (minimum 4 and max of 20 ): "))
        if length < 4 or length > 20:
            print("Password length should be at least 4 or a maximum of 20. Setting to default length of 8.")
            length = 8
    except ValueError:
        print("Invalid input. Setting password length to default of 8.")
        length = 8
    

    while True:
        special_char_choice = input("Include special characters? (y/n): ").strip().lower()
        use_special_chars = special_char_choice == 'y'
        if special_char_choice in ['y', 'n']:
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    

    password_generator = PasswordGenerator(use_special_chars, length)
    generated_password = password_generator.generate_password()
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()