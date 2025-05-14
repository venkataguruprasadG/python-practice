'''
Problem 69: Remove Duplicates from a List
Write a Python program that:

Takes a list of numbers as input from the user (numbers separated by spaces).

Removes all duplicate numbers from the list.

Prints the list of unique numbers in the order they first appeared.

Example 1:
Input:

text
Enter numbers: 1 2 2 3 4 4 5
Output:

text
Unique numbers: [1, 2, 3, 4, 5]
Example 2:
Input:

text
Enter numbers: 5 5 5 5 5
Output:

text
Unique numbers: [5]
Hints:
Use a list to store unique numbers.

Loop through the original list and add numbers to the unique list only if they are not already present.

Avoid using set() if you want to preserve the order.
'''

num_list=list(map(int, input("Enter your numbers: ").split()))

uniq_num_list=[]

for num in num_list:
    if num not in uniq_num_list:
        uniq_num_list.append(num)

print(f"unique Numbers are: {uniq_num_list}")