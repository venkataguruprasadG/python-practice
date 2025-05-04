'''
Problem 15: Sum of Squares
Write a Python program that takes a list of numbers (entered as space-separated values) from the user and prints the sum of the squares of those numbers.

Example:
Input:
2 3 4

Output:

text
Sum of squares: 29
'''

n=input("Enter the numbers: ")

num_list=n.split()

square_no=0
total=0

for i in num_list:
    square_no=int(i)*int(i)
    total=total+square_no

print(f"Sum of squares: {total}")



