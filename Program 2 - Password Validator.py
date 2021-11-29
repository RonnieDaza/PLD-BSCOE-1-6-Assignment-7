# Program 2 - Password Validator
# Create a program that checks if the password is valid.
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special character (!@#$%^&*()_+ etc)
# Example:
# Input:
# P@ssword+P@ssword13
# Output: Valid

# Steps
# 1. Import re.
import re

# 2. Ask the user for the password.
userPassword = input("Enter the password: ")

# 3. Set the passwordError variable to 0.
passwordError = 0

# 4. Test if the password is not greater than 15 letters.
if len(userPassword)<16:
    # 5. If it is true, then print a message to the user stating the error.
    print("Sorry, the password must be greater than 15 letters.")
    # 6. Because there is an error present, the passwordError variable becomes 1.
    passwordError = 1
# 7. Test if the password does not contain uppercase letters.
elif not re.search("[A-Z]", userPassword):
    # 8. If it is true, then print a message to the user stating the error.
    print("Sorry, the password must contain at least one capital letter (A-Z).")
    # 9. Because there is an error present, the passwordError variable becomes 1.
    passwordError = 1
# 10. Test if the password does not contain numbers.
elif not re.search("[0-9]", userPassword):