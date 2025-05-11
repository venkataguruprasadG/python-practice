'''
Problem 48: Palindrome Checker
Write a Python program that:

Takes a word/phrase as input from the user.

Checks if it’s a palindrome (reads the same forwards and backwards), ignoring spaces, punctuation, and case.

Prints "Yes, it's a palindrome!" or "No, it's not a palindrome."

Example 1:
Input:

text
Enter a word/phrase: A man, a plan, a canal: Panama!
Output:

text
Yes, it's a palindrome!
'''

word=input("Enter your word: ").lower()

cleaned=""
for char in word:
    if char.isalnum():
        cleaned+=char

reversed_word=cleaned[::-1]

if cleaned==reversed_word:
    print("Yes, it is palindrome")
else:
    print("No, Its not a plaindrome")

    