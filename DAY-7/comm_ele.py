'''
Problem 33: Find Common Elements in Two Lists
Write a Python program that:

Takes two space-separated lists of integers as input from the user (one after the other).

Finds and prints the list of unique elements that are common to both lists, sorted in ascending order.

Example:
Input:

text
Enter first list of numbers: 1 2 3 4 5 6 6 7
Enter second list of numbers: 4 5 6 7 8 9 6
Output:

text
Common elements: [4, 5, 6, 7]
'''

num1 = list(map(int, input("Enter your numbers for list 1: ").split()))
num2 = list(map(int, input("Enter your numbers for list 2: ").split()))

num1_set = set(num1)
num2_set = set(num2)

num_comm = sorted(num1_set & num2_set)

print(f"Common elements in the list: {num_comm}")
