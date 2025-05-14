'''
Problem 65: Word Frequency Counter
Write a Python program that:

Takes a sentence as input from the user.

Counts how many times each word appears in the sentence.

Prints the result as a dictionary, where the keys are words and the values are their counts.

Example 1:
Input:

text
Enter a sentence: the quick brown fox jumps over the lazy dog the fox
Output:

text
{'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
Example 2:
Input:

text
Enter a sentence: hello hello world
Output:

text
{'hello': 2, 'world': 1}
Hints:
Use .split() to break the sentence into words.

Use a dictionary to keep track of word counts.

You can use a for loop to update the counts.
'''

sentence=input("Enter your sentence: ").split()

num_dict={}

for word in sentence:
    if word not in num_dict:
        num_dict[word]=1
    else:
        num_dict[word]+=1

print(f"{num_dict}")