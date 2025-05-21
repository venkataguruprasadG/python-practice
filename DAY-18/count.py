'''
Challenge 87: Character Frequency Counter
Write a function called char_frequency that:

Accepts a string as input.

Returns a dictionary where each key is a character from the string, and its value is the number of times that character appears.

For example:

Input: "hello world"

Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
'''

def char_frequency(srt):
    freq={}
    for char in str:
        freq[char]=freq.get(char, 0) + 1
    return freq

print(char_frequency("Hello World"))