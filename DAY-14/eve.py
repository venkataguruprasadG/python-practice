'''
Problem 66: Filter Even Numbers from a List
Write a Python program that:

Takes a list of numbers as input from the user (numbers separated by spaces).

Filters out all the even numbers and stores them in a new list.

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
Enter numbers: 11 13 15
Output:

text
Even numbers: []
Hints:
Use .split() and map(int, ...) to process the input.

Use a for loop or list comprehension to filter even numbers (num % 2 == 0).
'''

numbers=list(map(int, input("Enter your numbers: ").split()))

eve_no_list=[]

for num in numbers:
    if num%2==0:
        eve_no_list.append(num)

print(f"Even numbers: {eve_no_list}")