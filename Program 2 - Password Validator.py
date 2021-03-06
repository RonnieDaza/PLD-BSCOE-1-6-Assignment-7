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
    # 11. If it is true, then print a message to the user stating the error.
    print("Sorry, the password must contain at least one number (0-9).")
    # 12. Because there is an error present, the passwordError variable becomes 1.
    passwordError = 1
# 13. Test if the password does not contain special characters.
elif not re.search("[ !@#$%^&*()_+=~`:;'<,>.?{[}|/-]", userPassword): # Excluded: "\] because these special characters disrupt the choices.
    # 14. If it is true, then print a message to the user stating the error.
    print("Sorry, the password must contain at least one special character ( !@#$%^&*()_+=~`:;'<,>.?{[}|/-).")
    # 15. Because there is an error present, the passwordError variable becomes 1.
    passwordError = 1

# 16. If the password does not match any conditions presented above, then the passwordError = 0 which means that the password is valid.
if (passwordError == 0):
    # 17. Print a message that states that the password is valid and show the valid password.
    print("The password is valid: ", userPassword)
else:
    # 18. If the password matches any conditions presented above, then the passwordError = 1 which means that the password is invalid.
    # 19. Print a message that states that the password is invalid and the user must try again.
    print("The password is invalid. Please try again.")