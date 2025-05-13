'''
Problem 62: Find the Maximum and Minimum in a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Finds and prints both the maximum and minimum numbers in the list.

Example 1:
Input:

text
Enter numbers: 5 3 8 2 9 1
Output:

text
Maximum: 9
Minimum: 1
Example 2:
Input:

text
Enter numbers: 17 23 5 89 42
Output:

text
Maximum: 89
Minimum: 5
Hints:
Use .split() to get the numbers from the input.

Convert the input strings to integers.

Use the built-in max() and min() functions, or try to find them using a loop for extra practice!
'''

num_list=input("Enter your numbers: ").split()

num_int=[int(num) for num in num_list]

num_max=max(num_int)

num_min=min(num_int)

print(f"maximum: {num_max}")
print(f"Minimum: {num_min}")