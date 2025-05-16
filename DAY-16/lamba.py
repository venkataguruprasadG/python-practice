'''
Challenge 79: Use Lambda to Square Numbers
Write a program that:

Uses a lambda function to square numbers in a list.

Uses the map() function to apply this lambda to the list `[1, 2,onverts the result to a list and prints it.

Expected Output:
text
[1, 4, 9, 16, 25]
Hints:
The lambda function should take one argument and return its square.

Use: map(lambda x: x*x, your_list)

Wrap the result in list() to display it.
'''

numbers = [1, 2, 3, 4, 5]

# Use lambda with map to square each number
squared = list(map(lambda x: x * x, numbers))

print(squared)  # Output: [1, 4, 9, 16, 25]
