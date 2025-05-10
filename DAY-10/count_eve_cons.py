'''
Problem 45: Count Vowels and Consonants
Write a Python program that:

Takes a sentence as input from the user.

Counts the number of vowels (a, e, i, o, u) and consonants (all other alphabetic characters).

Ignores spaces, numbers, and symbols.

Prints the counts in a user-friendly way.

Example 1:
Input:

text
Enter a sentence: Hello World 123
Output:

text
Vowels: 3 | Consonants: 7
'''

sentence=input("enter the sentence: ")

count_vowel=0
count_consonant=0

for char in sentence:
    if char.isalpha():
        if char.lower() in 'aeiou':
            count_vowel+=1
        else:
            count_consonant+=1

print(f"Vowels: {count_vowel} | Consonants: {count_consonant}")

