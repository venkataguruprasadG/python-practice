'''
Problem 16: Find the Minimum and Maximum
Write a Python program that takes a list of numbers (entered as space-separated values) from the user and prints the smallest and largest numbers in the list.

Example:
Input:
12 4 7 19 3 8

Output:

text
Minimum: 3
Maximum: 19
'''

n = input("Enter the numbers: ")
num_list = n.split()

# Convert string list to integer list
num_list = [int(i) for i in num_list]

# Initialize min and max to the first element
largest = num_list[0]
smallest = num_list[0]

for i in num_list:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(f"Maximum: {largest}")
print(f"Minimum: {smallest}")

