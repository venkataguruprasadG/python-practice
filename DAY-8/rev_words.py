'''
Problem 39: Reverse Words in a Sentence
Write a Python program that:

Takes a sentence as input from the user.

Reverses the order of the words (not the letters in the words).

Prints the resulting sentence.

Example:
Input:

text
Enter a sentence: Python is super fun to learn
Output:

text
Reversed sentence: learn to fun super is Python
'''

sentence=input("Enter your sentence: ").split()

rev_sen=sentence[::-1]

print(f"Reversed order: {' '.join(rev_sen)}")

