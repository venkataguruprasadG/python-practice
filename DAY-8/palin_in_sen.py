'''
Problem 40: Find Palindrome Words in a Sentence
Write a Python program that:

Takes a sentence as input from the user.

Finds all the words in the sentence that are palindromes (words that read the same forwards and backwards, like "madam" or "level").

Prints the list of palindrome words. If there are none, print "No palindrome words found."

Example 1:
Input:

text
Enter a sentence: Madam Arora teaches malayalam and level civic racecar
Output:

text
Palindrome words: ['Madam', '

Arora', 'malayalam', 'level', 'civic', 'racecar']
'''

sentence = input("Enter the sentence: ").split()

palindrome_words = []

for word in sentence:
    if word.lower() == word.lower()[::-1]:
        palindrome_words.append(word)

if palindrome_words:
    print(f"Palindrome words: {palindrome_words}")
else:
    print("No palindrome words found.")

