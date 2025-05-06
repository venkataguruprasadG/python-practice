'''
Problem 26: Most Frequent Word Finder
Write a Python program that:

Takes a sentence as input from the user.

Finds the word that appears most frequently in the sentence (ignore case).

Prints the most frequent word and how many times it appears.

If there are multiple words with the same highest frequency, print all of them (in alphabetical order).

Example:
Input:

text
The cat chased the mouse and the mouse ran from the cat
Output:

text
Most frequent word(s): ['the']
Frequency: 4
Another Input:

text
apple banana apple orange banana orange
Output:

text
Most frequent word(s): ['apple', 'banana', 'orange']
Frequency: 2
'''

sentence=input("Enter the sentence: ").lower()

words=sentence.split()

sen_dict={}

count=0

for char in words:
    sen_dict[char]=sen_dict.get(char,0)+1

max_freq=max(sen_dict.values())

most_frequent = []

for word, freq in sen_dict.items():
    if freq == max_freq:
        most_frequent.append(word)

most_frequent.sort()
print(most_frequent)

print(max_freq)



