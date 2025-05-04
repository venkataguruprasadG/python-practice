'''
Problem 12: Find the Largest Number

Write a Python program that takes a list of numbers (entered as space-separated values) and prints the largest number in the list.

Test Case:
Input: 3 8 2 15 6 → Output: 15
Input: -5 -2 -9 -1 → Output: -1
'''

s=input("enter the numbers: ")

strng_split=s.split()

num_list=[int(x) for x in strng_split]

largest=num_list[0]

for i in num_list:
    if i>largest:
        largest=i
print(largest)

