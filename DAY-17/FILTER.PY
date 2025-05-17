'''
Challenge 80: Filter Even Numbers
Write a program that:

Takes a list of numbers: [11, 22, 33, filter()` and a lambda function to keep only the even numbers

Converts the result to a list and prints it

Expected Output:
text
[22, 44, 66]
Hints:
Even numbers have number % 2 == 0

Use: filter(lambda x: x % 2 == 0, numbers)
'''

numbers=[11, 22, 33]

even=list(filter(lambda x: x % 2 == 0, numbers))

print(even)