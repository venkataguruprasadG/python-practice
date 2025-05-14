'''
Problem 64: Find Common Elements in Two Lists
Write a Python program that:

Takes two lists of numbers as input from the user (numbers separated by spaces).

Finds and prints the common elements between the two lists (no duplicates in the result).

Example 1:
Input:

text
Enter first list: 1 2 3 4 5
Enter second list: 4 5 6 7 8
Output:

text
Common elements: [4, 5]
Example 2:
Input:

text
Enter first list: 10 20 30
Enter second list: 40 50 60
Output:

text
Common elements: []
Hints:
Use .split() and int() to process the input.

Use set() to find common elements easily.

Convert the result back to a list if you want to print as a list.
'''

num1_list = list(map(int, input("Enter first list: ").split()))
num2_list = list(map(int, input("Enter second list: ").split()))

comm_num = []

for num1 in num1_list:
    for num2 in num2_list:
        if num1 == num2 and num1 not in comm_num:  # to avoid duplicates
            comm_num.append(num1)

print(f"Common elements are: {comm_num}")
