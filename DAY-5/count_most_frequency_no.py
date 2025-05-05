'''
Problem 21: Find the Most Frequent Number
Write a Python program that takes a list of numbers (space-separated) and prints the number that appears most frequently along with its count.

Example:
Input:
4 5 2 4 3 4 2 2 2

Output:

text
Most frequent number: 2
Count: 4
'''
n = input("Enter your numbers: ")
num_list = [int(x) for x in n.split()]

max_count = 0
most_frequent = None

for i in num_list:
    count = 0
    for j in num_list:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        most_frequent = i

print(f"Most frequent number: {most_frequent}")
print(f"Count: {max_count}")
