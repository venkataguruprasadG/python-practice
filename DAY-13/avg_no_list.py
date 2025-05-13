'''
Problem 59: Calculate the Average of Numbers in a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Calculates and prints the average (mean) of those numbers.

Example 1:
Input:

text
Enter numbers: 10 20 30 40 50
Output:

text
The average is: 30.0
Example 2:
Input:

text
Enter numbers: 5 8 12
Output:

text
The average is: 8.333333333333334
Hints:
Use .split() to get the numbers from the input.

Convert each input to an integer or float.

Use sum() and len() to calculate the average.
'''

num_list=input("enter your numbers").split()

num_list_int=[int(num) for num in num_list]

num_list_sum=sum(num_list_int)

num_list_length=len(num_list_int)

avg=num_list_sum/num_list_length

print(f"the average is: {avg}")