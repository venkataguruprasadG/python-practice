'''
Problem 22: Dictionary Frequency Counter
Problem:
Write a Python program that takes a sentence as input from the user, splits it into words, and then prints a dictionary where the keys are the words and the values are the number of times each word appears in the sentence.

Example:
Input:
the quick brown fox jumps over the lazy dog the dog was not amused

Output:

text
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}
'''

sentence = input("Enter your sentence: ")
words = sentence.split()
frq_dict = {}

for word in words:
    frq_dict[word] = frq_dict.get(word, 0) + 1

print(frq_dict)

