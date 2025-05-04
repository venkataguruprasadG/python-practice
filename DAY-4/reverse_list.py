'''
Problem 17: Reverse the List
Write a Python program that takes a list of numbers (entered as space-separated values) from the user and prints the numbers in reverse order (all on one line, space-separated).

Example:
Input:
5 10 3 8 2

Output:

text
2 8 3 10 5
'''

num=input("Enter you list numbers you want to insert: ")

num_list=num.split()

print(*num_list[::-1])