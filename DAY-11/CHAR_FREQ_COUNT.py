'''
Problem 47: Character Frequency Counter
Write a Python program that:

Takes a word as input from the user (case-insensitive).

Counts how many times each character appears in the word.

Prints the result as Character: Count for each unique character.

Example 1:
Input:

text
Enter a word: hello
Output:

text
h: 1
e: 1
l: 2
o: 1
'''

word=input("Enter your word: ")

char_count={}

for char in word:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1

for char, count in char_count.items():
    print(f"{char}: {count}")

    