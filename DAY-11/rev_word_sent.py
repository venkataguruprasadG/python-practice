'''
Problem 49: Reverse Each Word in a Sentence
Write a Python program that:

Takes a sentence as input from the user.

Reverses each word individually while keeping the original word order.

Prints the modified sentence.

Example 1:
Input:

text
Enter a sentence: Python is fun
Output:

text
nohtyP si nuf
'''

sentence=input("Enter your sentence: ")

words=sentence.split()

reversed_word=[]

for word in words:
    reversed_word=word[::-1]
    reversed_word.append(reversed_word)

result = " ".join(reversed_word)
