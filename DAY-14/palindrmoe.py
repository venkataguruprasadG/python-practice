'''
Problem 63: Check if a String is a Palindrome
Write a Python program that:

Takes a string input from the user.

Checks if the string is a palindrome (reads the same forwards and backwards).

Ignores spaces and is case-insensitive.

Prints "Palindrome" if it is, or "Not a palindrome" if it isn’t.

Example 1:
Input:

text
Enter a string: Race car
Output:

text
Palindrome
Example 2:
Input:

text
Enter a string: Hello World
Output:

text
Not a palindrome
Hints:
Use .replace(" ", "") to remove spaces.

Use .lower() to ignore case.

Compare the cleaned string to its reverse ([::-1]).
'''

sentence=input("Enter a sentence: ").lower()

clean_sentence=sentence.replace(" ","")

if clean_sentence==clean_sentence[::-1]:
    print("Yes, The given string is a palindrome")
else:
    print("NO the given the string is not palindrome")

    