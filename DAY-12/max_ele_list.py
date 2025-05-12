'''
Problem 53: Find the Largest Number in a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Finds and prints the largest number in the list.

Example 1:
Input:

text
Enter numbers: 5 12 7 3 9
Output:

text
The largest number is: 12
Example 2:
Input:

text
Enter numbers: -2 -8 -1 -10
Output:

text
The largest number is: -1
Hints:
Use .split() to get the numbers from the input.

Convert each input to an integer.

Use a loop to find the largest number, or use Python’s built-in max() function.
'''

num_list=input("Enter your numbers: ").split()

num_list=[int(num) for num in num_list] #it will covert the strings into the integers here

num_max=max(num_list)

print(f"The largest number: {num_max}")