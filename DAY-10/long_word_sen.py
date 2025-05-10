'''
Problem 46: Find the Longest Word in a Sentence
Write a Python program that:

Takes a sentence as input from the user.

Finds and prints the longest word in the sentence.

If there are multiple words with the same maximum length, print any one of them.

Example 1:
Input:

text
Enter a sentence: Coding in Python is awesome
Output:

text
The longest word is: awesome
'''

sentence=input("Enter your sentence: ").split()

longest_word=0

for word in sentence:
    if len(word)>len(longest_word):
        longest_word=word

print(f"The longest word is: {longest_word}")