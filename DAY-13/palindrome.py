'''
Problem 58: Check if a String is a Palindrome
Write a Python program that:

Takes a string input from the user.

Checks if the string is a palindrome (reads the same forwards and backwards, ignoring spaces and case).

Prints whether the string is a palindrome or not.

Example 1:
Input:

text
Enter a string: madam
Output:

text
The string is a palindrome.
Example 2:
Input:

text
Enter a string: Race car
Output:

text
The string is a palindrome.
Example 3:
Input:

text
Enter a string: Python
Output:

text
The string is not a palindrome.
Hints:
Remove spaces and convert the string to lowercase.

Compare the cleaned string to its reverse (string[::-1]).
'''

sentence=input("Enter your setence: ").lower()

remove_spaces_Str=sentence.replace(" ","")

reverse_str=remove_spaces_Str[::-1]

if remove_spaces_Str==reverse_str:
    print(f"The string is a palidrome: {sentence}")
else:
    print(f"The string is not a palidrome: {sentence}")
