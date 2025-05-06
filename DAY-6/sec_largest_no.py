'''
Problem 29: Second Largest Number Finder
Write a Python program that:

Takes a list of integers as input from the user (space-separated).

Finds and prints the second largest unique number in the list.

If there is no second largest (i.e., all numbers are the same), print a message saying so.

Example 1:
Input:

text
Enter numbers: 5 3 9 1 9 7 5
Output:

text
Second largest number: 7
'''

num=input("Enter your numbers: ")

num_list=[int(x) for x in num.split()]

uniq_list=list(set(num_list))

largest_no=num_list[0]

print(f"Unique elements list: {uniq_list}")

if(len(uniq_list)<2):
    print("There is no second largest integer")
else:
    uniq_list.sort(reverse=True)
    print(f"Second largest number: {uniq_list[1]}")