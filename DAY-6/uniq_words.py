'''
Problem 25: Unique Words Finder
Write a Python program that:

Takes a sentence as input from the user.

Prints a sorted list of all unique words in the sentence (ignore case).

Example:
Input:

text
The quick brown fox jumps over the lazy dog the dog was not amused
Output:

text
['amused', 'brown', 'dog', 'fox', 'jumps', 'lazy', 'not', 'over', 'quick', 'the', 'was']
'''

sentence=input("Enter the sentence: ")

sen_list=sentence.lower().split()

uniq_list=sorted(set(sen_list))

print(uniq_list)

