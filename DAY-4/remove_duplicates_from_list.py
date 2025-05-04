'''
Problem 18: Remove Duplicates from a List
Write a Python program that takes a list of numbers (entered as space-separated values) from the user and prints the list with duplicates removed, preserving the original order.

Example:
Input:
5 3 8 3 9 5 2 8

Output:

text
5 3 8 9 2
'''

num=input("Enter your numbers: ")

num_list=num.split()

unique_list=[]

for i in num_list:
    if i not in unique_list:
        unique_list.append(i)

print(*unique_list)