'''
Problem 42: Words with Repeated Letters
Write a Python program that:

Takes a sentence as input from the user.

Finds all words in the sentence that contain at least one letter that appears more than once in that word (case-insensitive).

Prints the list of such words. If none are found, print "No words with repeated letters."

Example 1:
Input:

text
Enter a sentence: Hello apple tree world
Output:

text
Words with repeated letters: ['Hello', 'apple', 'tree']
'''

sentence=input("Enter your sentence: ").split()

repeated_words=[]

for word in sentence:
    seen=set()
    has_repeat=False
    for letter in word.lower():
        if letter.isalpha():
            if letter in seen:
                has_repeat=True
                break
            seen.add(letter)
    if has_repeat:
        repeated_words.append(word)

if repeated_words:
    print(f"Words with repeated letters: {repeated_words}")
else:
    print("No words with repeated letters.")

