'''
Problem 41: Sum of Digits in Each Word
Write a Python program that:

Takes a sentence as input from the user.

For each word in the sentence, calculates the sum of all digit characters in that word (ignore non-digit characters).

Prints each word along with the sum of its digits. If a word has no digits, the sum should be 0.

Example:
Input:

text
Enter a sentence: py3th0n c0d1ng d4y9
Output:

text
Word: py3th0n, Sum of digits: 3
Word: c0d1ng, Sum of digits: 1
Word: d4y9, Sum of digits: 13
'''

sentence=input("Enter your sentence: ").split()

for word in sentence:
    digit_sum=0
    for char in word:
        if char.isdigit():
            digit_sum+=int(char)
    print(f"Word: {word}, Sum of digits: {digit_sum}")