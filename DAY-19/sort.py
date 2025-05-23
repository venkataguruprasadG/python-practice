'''
Challenge 90: Sort by Last Character
Task:
Given a list of words, use a lambda function to sort the list by the last character of each word.
'''

words = ["banana", "apple", "cherry", "date"]

# Sort using lambda to get the last character
sorted_words = sorted(words, key=lambda word: word[-1])

print(sorted_words)  # Output: ['banana', 'apple', 'date', 'cherry']
