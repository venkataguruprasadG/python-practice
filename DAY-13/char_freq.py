'''
Problem 61: Character Frequency in a String
Write a Python program that:

Takes a string input from the user.

Counts how many times each character appears in the string.

Prints each character along with its frequency.

Example 1:
Input:

text
Enter a string: hello world
Output:

text
h: 1
e: 1
l: 3
o: 2
 : 1
w: 1
r: 1
d: 1
Example 2:
Input:

text
Enter a string: programming
Output:

text
p: 1
r: 2
o: 1
g: 2
a: 1
m: 2
i: 1
n: 1
Hints:
Use a dictionary to store character counts.

Loop through each character in the string.

Update the count in the dictionary.
'''

sentence=input("Enter your sentece: ")

word_dict={}

for word in sentence:
    if word in word_dict:
        word_dict[word]+=1
    else:
        word_dict[word]=1

for word,value in word_dict.items():
    print(f"{word}|{value}")