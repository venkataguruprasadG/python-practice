'''
Problem 50: Password Strength Checker
Write a Python program that:

Takes a password as input.

Checks if it meets these criteria:

At least 8 characters long.

Contains at least 1 uppercase letter.

Contains at least 1 lowercase letter.

Contains at least 1 digit.

Contains at least 1 special character (e.g., !, @, #, $, etc.).

Prints "Strong" if all criteria are met, or "Weak" if any fail.

Example 1:
Input:

text
Enter a password: Hello123!
Output:

text
Strong
'''

password=input("Enter a password: ")

has_upper=False
has_lower=False
has_digit=False
has_special=False
has_length=False

for char in password:
    if char.isupper():
        has_upper=True
    if char.islower():
        has_lower=True
    if char.isdigit():
        has_digit=True
    if not char.isalnum():
        has_special=True
    
has_length=len(password)>=8

if all([has_upper,has_lower,has_digit,has_special,has_length]):
    print("Password is strong")
else:
    print("weak")