'''
Problem 36: Count Words That Start With a Vowel
Write a Python program that:

Takes a sentence as input from the user.

Counts how many words in the sentence start with a vowel (a, e, i, o, u - case-insensitive).

Prints the count and a list of those words.

Example:
Input:

text
Enter a sentence: An elephant is on its own island under an oak tree.
Output:

text
Words starting with a vowel: ['An', 'elephant', 'is', 'on', 'its', 'own', 'island', 'under', 'an', 'oak']
Count: 10
'''

words = input("Enter your sentence: ").split()

result = []
count = 0

for word in words:
    if word[0].lower() in 'aeiou':
        result.append(word)
        count += 1

print(f"Words starting with a vowel: {result}")
print(f"Count: {count}")
