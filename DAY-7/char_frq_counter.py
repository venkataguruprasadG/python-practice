'''
Problem 30: Character Frequency Counter
Write a Python program that:

Takes a string input from the user.

Counts the frequency of each character (ignore spaces and case).

Prints the character(s) with the highest frequency and the frequency value.

Example 1:
Input:

text
Enter a string: Success is not final, failure is not fatal.
Output:

text
Most frequent character(s): ['s']
Frequency: 6
'''

sentence=input()

char_dict={}

for chars in sentence.lower():
    if chars.isalpha():
        char_dict[chars]=char_dict.get(chars,0)+1

if char_dict:
    max_freq = max(char_dict.values())
    most_frequent = [char for char, freq in char_dict.items() if freq == max_freq]
    most_frequent.sort()
    print(f"Most frequent character(s): {most_frequent}")
    print(f"Frequency: {max_freq}")
else:
    print("No alphabetic characters found.")
