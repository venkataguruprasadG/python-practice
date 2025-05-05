'''
Problem 19: Find the Second Largest Number
Write a Python program that takes a list of numbers (entered as space-separated values) from the user and prints the second largest number in the list.

Example:
Input:
5 9 2 7 9 3

Output:

text
Second largest: 7
'''

n=input("Enter you numbers: ")

num_list=[int(x) for x in n.split()]

unique_nums=list(set(num_list))

largest=num_list[0]

if len(unique_nums) < 2:
    print("There is no second largest number: ")
else:
    unique_nums.sort(reverse=True)
    print(f"Second Largest: {unique_nums[1]}")


