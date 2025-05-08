'''
Problem 35: Find the Longest Word(s) in a Sentence
Write a Python program that:

Takes a sentence as input from the user.

Finds the longest word(s) in the sentence.

Prints a list of the longest word(s) (if there are ties, print all of them) and their length.

Example:
Input:

text
Enter a sentence: The quick brown fox jumps over the lazy dog
Output:

text
Longest word(s): ['quick', 'brown', 'jumps']
Length: 5
'''

words=input("Enter your sentence: ").split()

if words:
    max_length=max(len(word) for word in words)
    longest_words=[word for word in words if len(word)==max_length]
    print(f"Longest words: {longest_words}")
    print(f"Length: {max_length}")
else:
    print(f"No words are found in the sentence")
    