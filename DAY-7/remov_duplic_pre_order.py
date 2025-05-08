'''
Problem 34: Remove Duplicates and Preserve Order
Write a Python program that:

Takes a list of integers as input from the user (space-separated).

Removes all duplicate numbers but preserves the original order of their first appearance.

Prints the resulting list.

Example:
Input:

text
Enter numbers: 4 5 6 4 7 5 8 6 9
Output:

text
List after removing duplicates: [4, 5, 6, 7, 8, 9]
'''

num_list = [4, 5, 6, 4, 7, 5, 8, 6, 9]

seen = set()
result = []

for num in num_list:
    if num not in seen:
        result.append(num)
        seen.add(num)

print(f"Result list: {result}")



