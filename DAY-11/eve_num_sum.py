'''
Problem 52: Sum of Even Numbers in a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Calculates and prints the sum of all even numbers in the list.

Example 1:
Input:

text
Enter numbers: 1 2 3 4 5 6
Output:

text
Sum of even numbers: 12
'''

num_list=input("Enter your numbers: ").split()

total=0

for num in num_list:
    if int(num)%2==0:
        total+=int(num)

print(f"Sum of even numbers: {total}")