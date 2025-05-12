'''
Problem 56: Remove Duplicates from a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Removes all duplicate numbers, keeping only the first occurrence of each.

Prints the new list without duplicates.

Example 1:
Input:

text
Enter numbers: 1 2 2 3 4 3 5 1
Output:

text
List after removing duplicates: [1, 2, 3, 4, 5]
Example 2:
Input:

text
Enter numbers: 7 8 9 7 8 10
Output:

text
List after removing duplicates: [7, 8, 9, 10]
Hints:
Use a new list to store unique numbers.

Loop through the input list and add each number to the new list only if it’s not already there.
'''

num_list=input("Enter your numbers: ").split()

new_list=[]

for num in num_list:
    if num not in new_list:
        new_list.append(num)

print(f"List after removing duplicates: {new_list}")