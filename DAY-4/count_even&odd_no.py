'''
Problem 14: Count Even and Odd Numbers
Write a Python program that takes a list of numbers (entered as space-separated values) from the user.
Print how many numbers are even and how many are odd.

Example:
Input:
4 7 2 9 10 13

Output:

text
Even numbers: 3
Odd numbers: 3
'''

num_list = []

n = int(input("How many numbers will you enter? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    num_list.append(num)

count_even = 0
count_odd = 0

for j in num_list:
    if j % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Even numbers: {count_even}")
print(f"Odd numbers: {count_odd}")




