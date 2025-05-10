'''
Problem 43: Find Words with All Vowels
Write a Python program that:

Takes a sentence as input from the user.

Finds all words in the sentence that contain all five vowels (a, e, i, o, u) at least once (case-insensitive).

Prints the list of such words. If none are found, print "No words with all vowels."

Example 1:
Input:

text
Enter a sentence: Education is a beautiful journey and sequoia is a unique tree
Output:

text
Words with all vowels: ['Education', 'beautiful', 'sequoia']
'''

sentence=input("Enter the sentence: ").split()

vowel_list=[]
vowels=set('aeiou')

for word in sentence:
    letters=set(word.lower())
    if vowels.issubset(letters):
        vowel_list.append(word)

if vowel_list:
    print(f"Words with all vowels: {vowel_list}")
else:
    print(f"No Words with all vowels")

print(f"Words with all vowels: {vowel_list}")

