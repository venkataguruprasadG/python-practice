'''
Problem 68: Find the Maximum and Minimum in a List
Write a Python program that:

Takes a list of numbers as input from the user (numbers separated by spaces).

Finds the maximum and minimum numbers in the list using a function.

Prints both the maximum and minimum values.

Example 1:
Input:

text
Enter numbers: 5 9 2 8 1 7
Output:

text
Maximum: 9
Minimum: 1
Example 2:
Input:

text
Enter numbers: -3 0 4 2 -8
Output:

text
Maximum: 4
Minimum: -8
Hints:
Use map(int, ...) to convert input to integers.

You can use built-in functions (max(), min()) or write your own logic with a loop.
'''

num_list=list(map(int, input("Enter your numbers: ").split()))

num_max=max(num_list)

num_min=min(num_list)

print(f"Maximum: {num_max}")
print(f"Minimum: {num_min}")