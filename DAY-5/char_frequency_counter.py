'''
Problem 23: Character Frequency Counter (Ignore Case and Spaces)
Write a Python program that takes a sentence as input and prints a dictionary where the keys are the characters (letters only, ignore spaces and case) and the values are the number of times each character appears.

Example:
Input:

text
The quick brown fox jumps over the lazy dog
Output:

text
{'t': 2, 'h': 2, 'e': 3, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
'''

sentence=input("Enter your sentence: ")

char_dict={}

for chars in sentence.lower():
    if chars.isalpha():
        char_dict[chars]=char_dict.get(chars,0)+1

print(char_dict)
