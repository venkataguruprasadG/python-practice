'''
Problem 51: Duplicate Number Checker
Write a Python program that:

Takes a list of numbers as input (e.g., `[1,

Checks if there are any duplicate numbers in the list.

Prints "Duplicates found!" or "No duplicates".

Example 1:
Input:

text
Enter numbers: 1 2 3 4 5
Output:

text
No duplicates
'''

numbers = input("Enter your numbers: ").split()

num_dict = {}

for num in numbers:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

duplicates_found = False
for count in num_dict.values():
    if count > 1:
        duplicates_found = True
        break

if duplicates_found:
    print("Duplicates found!")
else:
    print("No duplicates")
