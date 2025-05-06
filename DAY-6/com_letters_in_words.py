'''
Problem 28: Common Letters in Words
Write a Python program that:

Takes two words as input from the user.

Finds all the letters that appear in both words (ignore case).

Prints the common letters in alphabetical order as a list.

Example:
Input:

text
Enter first word: Python
Enter second word: Hypnotic
Output:

text
Common letters: ['h', 'n', 'o', 'p', 't', 'y']
'''

word1=input("Enter your first word: ")

word2=input("Enter your second word: ")

word1_set=set(word1)

word2_set=set(word2)

common_letters=word1_set & word2_set

result=sorted(list(common_letters))

print(f"Common letters: {result}")

