'''
Problem 60: Extract Even Numbers from a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Creates a new list containing only the even numbers using a list comprehension.

Prints the list of even numbers.

Example 1:
Input:

text
Enter numbers: 1 2 3 4 5 6 7 8
Output:

text
Even numbers: [2, 4, 6, 8]
Example 2:
Input:

text
Enter numbers: 11 13 15 18 20
Output:

text
Even numbers: [18, 20]
Hints:
Use a list comprehension with an if condition to check if a number is even (num % 2 == 0).

Don’t forget to convert input strings to integers!
'''

num_list=input("Enter your numbers: ").split()

even_list=[int(num) for num in num_list if num%2==0]

print(f"Even numebrs: {even_list}")