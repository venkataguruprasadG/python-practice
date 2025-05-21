'''
Challenge 88: Longest Word Finder
Write a function called longest_word that:

Accepts a sentence (string) as input.

Returns the longest word in that sentence.

If there are multiple words of the same maximum length, return the first one.

For example:

Input: "The quick brown fox jumps over the lazy dog"

Output: "quick"

Input: "I love programming in Python"

Output: "programming"
'''

def longest_word(string):
    string_list=string.split()
    return max(string_list, key=len)

print(longest_word("I love programming in Python"))