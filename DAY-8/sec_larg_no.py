'''
Problem 38: Find the Second Largest Number
Write a Python program that:

Takes a list of integers as input from the user (space-separated).

Finds and prints the second largest unique number in the list.

If there is no second largest (e.g., all numbers are the same), print "No second largest number found."

Example 1:
Input:

text
Enter numbers: 10 20 4 45 99 99 20
Output:

text
Second largest number: 45
'''

num=list(map(int, input("Enter your numbers: "))).split()

num_set=set(num)

if len(num_set)<2:
    print(f"No Second Largest number is found.")
else:
    num_set.remove(max(num_set))
    second_largest=max(num_set)
    print(f"Second largest number in the list: {second_largest}")

