'''
Problem 32: Palindrome Checker for a List of Words
Write a Python program that:

Takes a space-separated list of words as input from the user.

Checks each word to see if it is a palindrome (reads the same forwards and backwards, case-insensitive).

Prints two lists:

One with all the palindromic words (in the order they appeared).

One with all the non-palindromic words (in the order they appeared).

Example:
Input:

text
Enter words: madam racecar apple level noon banana
Output:

text
Palindromes: ['madam', 'racecar', 'level', 'noon']
Non-palindromes: ['apple', 'banana']
'''

user_words = input("Enter your words: ").split()

palindrome_list = []
non_palind_list = []

for word in user_words:
    if word.lower() == word.lower()[::-1]:
        palindrome_list.append(word)
    else:
        non_palind_list.append(word)

print(f"Palindrome list: {palindrome_list}")
print(f"Non-palindrome list: {non_palind_list}")






