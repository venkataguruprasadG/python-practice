'''
Problem 57: Count Vowels in a String
Write a Python program that:

Takes a string input from the user.

Counts and prints how many vowels (a, e, i, o, u) are present in the string.

Example 1:
Input:

text
Enter a string: Hello World
Output:

text
Number of vowels: 3
Example 2:
Input:

text
Enter a string: Python is awesome!
Output:

text
Number of vowels: 6
Hints:
Convert the input string to lowercase to make checking easier.

Use a loop to check each character.

You can use a variable to keep the count.
'''

sentence=input("Enter your sentence: ")

vowel_count=0

for char in sentence.lower():
    if char in 'aeiou':
        vowel_count+=1

print(f"number of vowels: {vowel_count}")