'''
Challenge 91: Filter Palindromes
Task:
Given a list of words, use a lambda function with filter() to find all the palindromes (words that read the same forwards and backwards).
'''

words=["level","python","radar","world"]

palindromes=list(filter(lambda word: word == word[::-1], words))

print(palindromes)

