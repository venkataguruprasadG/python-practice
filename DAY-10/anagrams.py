'''
Problem 44: Check for Anagrams
Write a Python program that:

Takes two words/phrases as input from the user (case-insensitive).

Checks if they are anagrams (contain the same letters in any order, ignoring spaces and punctuation).

Prints "Yes, they are anagrams!" or "No, they are not anagrams."

Example 1:
Input:

text
Enter first word: listen
Enter second word: silent
Output:

text
Yes, they are anagrams!
'''

word1 = input("Enter your word1: ")
word2 = input("Enter your word2: ")

# Convert to lowercase
word1 = word1.lower()
word2 = word2.lower()

# Remove spaces
word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")

# Sort the letters
sorted1 = sorted(word1)
sorted2 = sorted(word2)

if sorted1 == sorted2:
    print("Yes, they are anagrams!")
else:
    print("No, they are not anagrams.")



